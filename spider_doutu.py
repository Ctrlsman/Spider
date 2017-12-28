import urllib.request
import requests
from bs4 import BeautifulSoup
import time

urls = ['http://www.doutula.com/article/list/?page={}'.format(str(i)) for i in range(4, 500)]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}


def get_url(url):
    time.sleep(2)
    info = requests.get(url, headers)
    info_text = info.text
    soup = BeautifulSoup(info_text, 'html')
    all_a = soup.find_all('a', class_='list-group-item')
    down_list = []
    for link in all_a:
        img_html = link.get('href')
        down_list.append(img_html)
    return down_list


def get_img(img_list):
    down_list = img_list
    all_img_link_list = []
    all_img_title = []
    for item in down_list:
        main_info = requests.get(item)
        main_content = main_info.text
        s = BeautifulSoup(main_content, 'html')
        all_img = s.select('div[class="artile_des"] > table > tbody > tr > td > a > img')
        for i in all_img:
            all_img_title.append(i.get('alt'))
            if i.get('src')[:5] == 'http:':
                all_img_link_list.append(i.get('src'))
            else:
                all_img_link_list.append('http:' + i.get('src'))
    return all_img_title, all_img_link_list


def down(title, link):
    file_path = '/home/zds/Documents/myself'
    try:
        for t, l in zip(title, link):
            urllib.request.urlretrieve(l, file_path + t + '.jpg')
    except Exception as e:
        pass


count = 1
for url in urls:
    print("正在爬取第%s页" % count)
    count += 1
    img_list = get_url(url)
    title, link = get_img(img_list)
    down(title, link)
    # for t, l in zip(title, link):
    #     th = threading.Thread(target=down,args=(t,l))   #多线程爬取数据不完整
    #     th.start()
