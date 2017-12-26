import aiohttp
import asyncio
from aiohttp import web
import requests
from bs4 import BeautifulSoup
import time

URL = 'https://bj.5i5j.com/zufang/'


def run():
    urls = ["https://bj.5i5j.com/zufang/n{}/".format(i) for i in range(1, 20)]
    info = {
        'title': '',
        'price': '',
        'url': '',
        'img': [],
        'tips': ''
    }
    for l in urls:
        resp = requests.get(l)
        soup = BeautifulSoup(resp.text, 'html')
        print(soup)


run()


async def index():
    return web.Response()


def init():
    app = web.Application()
    app.router.add_get('/index', index)
    return app


if __name__ == '__main__':
    app = init()
    web.run_app(app, host='127.0.0.1', port=8080)