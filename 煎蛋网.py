import urllib.request
import requests
from bs4 import BeautifulSoup
import time

urls=['http://jandan.net/pic/page-{}#comments'.format(str(i)) for i in range(1,99)]
# urls=['http://jandan.net/ooxx/page-{}#comments'.format(str(i)) for i in range(1,99)]


def get_jiandan(url):
    content = requests.get(url)    #访问请求，返回一个response
    # time.sleep(1)
    content_text = content.text     #得到文本
    soup = BeautifulSoup(content_text,'lxml')    #用lxml
    folder_path = 'D:/pic2/'
    img_downlink_list = []
    # img_lables = soup.find_all('img')             #去网页中查看元素找到所有的img标签,不是真正的图片
    img_lables = soup.select('div > div.text > p > a')  #找到真正的图片下载地址，可下载gif图片
    for img_lable in img_lables:
        img_downlink_list.append('http:'+img_lable.get('href'))  #因为网页中没有加协议头，手工加上

    for item in img_downlink_list:
        try:
            urllib.request.urlretrieve(item,folder_path + item[-10:])
        except Exception:
            pass
count = 1
for url in urls:
    print("正在下载第%s页"%count)
    get_jiandan(url)
    count+=1