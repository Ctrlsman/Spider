#!/usr/bin/env python
# -*- coding:utf-8 -*-
from twisted.web.client import getPage, defer
from twisted.internet import reactor
import queue


class Response(object):
    def __init__(self, body, request):
        self.body = body
        self.request = request
        self.url = request.url

    @property
    def text(self):
        return self.body.decode('utf-8')


class Request(object):
    def __init__(self, url, callback=None):
        self.url = url
        self.callback = callback


class Scheduler(object):
    def __init__(self, engine):
        self.q = queue.Queue()
        self.engine = engine

    def enqueue_request(self, request):
        self.q.put(request)

    def next_request(self):
        try:
            req = self.q.get(block=False)
        except Exception as e:
            req = None

        return req

    def size(self):
        return self.q.qsize()


class ExecutionEngine(object):
    def __init__(self):
        self._closewait = None
        self.running = True
        self.start_requests = None
        self.scheduler = Scheduler(self)

        self.inprogress = set()

    def check_empty(self, response):
        if not self.running:
            self._closewait.callback('......')

    def _next_request(self):
        while self.start_requests:
            try:
                request = next(self.start_requests)
            except StopIteration:
                self.start_requests = None
            else:
                self.scheduler.enqueue_request(request)

        while len(self.inprogress) < 5 and self.scheduler.size() > 0:  # 最大并发数为5

            request = self.scheduler.next_request()
            if not request:
                break

            self.inprogress.add(request)
            d = getPage(bytes(request.url, encoding='utf-8'))
            d.addBoth(self._handle_downloader_output, request)
            d.addBoth(lambda x, req: self.inprogress.remove(req), request)
            d.addBoth(lambda x: self._next_request())

        if len(self.inprogress) == 0 and self.scheduler.size() == 0:
            self._closewait.callback(None)

    def _handle_downloader_output(self, body, request):
        """
        获取内容，执行回调函数，并且把回调函数中的返回值获取，并添加到队列中
        :param response: 
        :param request: 
        :return: 
        """
        import types

        response = Response(body, request)
        func = request.callback or self.spider.parse
        gen = func(response)
        if isinstance(gen, types.GeneratorType):
            for req in gen:
                self.scheduler.enqueue_request(req)

    @defer.inlineCallbacks
    def start(self):
        self._closewait = defer.Deferred()
        yield self._closewait

    @defer.inlineCallbacks
    def open_spider(self, spider, start_requests):
        self.start_requests = start_requests
        self.spider = spider
        yield None
        reactor.callLater(0, self._next_request)


class Crawler(object):
    def __init__(self, spidercls):
        self.spidercls = spidercls

        self.spider = None
        self.engine = None

    @defer.inlineCallbacks
    def crawl(self):
        self.engine = ExecutionEngine()
        self.spider = self.spidercls()
        start_requests = iter(self.spider.start_requests())
        start_requests = iter(start_requests)
        yield self.engine.open_spider(self.spider, start_requests)
        yield self.engine.start()


class CrawlerProcess(object):
    def __init__(self):
        self._active = set()
        self.crawlers = set()

    def crawl(self, spidercls, *args, **kwargs):
        crawler = Crawler(spidercls)

        self.crawlers.add(crawler)
        d = crawler.crawl(*args, **kwargs)
        self._active.add(d)
        return d

    def start(self):
        dl = defer.DeferredList(self._active)
        dl.addBoth(self._stop_reactor)
        reactor.run()

    def _stop_reactor(self, _=None):
        reactor.stop()


class Spider(object):
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url)


class ChoutiSpider(Spider):
    name = "chouti"
    start_urls = [
        'http://dig.chouti.com/',
    ]

    def parse(self, response):
        print(response.text)


class CnblogsSpider(Spider):
    name = "cnblogs"
    start_urls = [
        'http://www.cnblogs.com/',
    ]

    def parse(self, response):
        print(response.text)


if __name__ == '__main__':

    spider_cls_list = [ChoutiSpider, CnblogsSpider]

    crawler_process = CrawlerProcess()
    for spider_cls in spider_cls_list:
        crawler_process.crawl(spider_cls)

    crawler_process.start()