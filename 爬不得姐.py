import requests
import urllib.request
from bs4 import BeautifulSoup
import time

urls = ['http://www.budejie.com/tag/117/{}'.format(str(i)) for i in range(1,20)]


def get_video(url):
    source_code = requests.get(url)
    time.sleep(1)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')
    find_titles = soup.select('div.j-r-list-tool-r.j-r-list-tool-cc > ul > li[title="下载视频"] ')
    find_downlinks = soup.select('div.j-r-list-tool-r.j-r-list-tool-cc > ul > li[title="下载视频"] > a')
    titles =[]
    video_downloadlink=[]
    for i in find_titles:
        titles.append(i.get('data-text'))
    for j in find_downlinks:
        video_downloadlink.append(j.get('href'))

    folder_path = 'D:/f/'
    # reg = r'data-mp4="(.*?)"'
    # video_downloadlink= re.findall(reg,plain_text)
    for dl,title in zip(video_downloadlink,titles):
        if '/' not in title:
            try:
                urllib.request.urlretrieve(dl,folder_path+''+title+'.mp4')
            except Exception:
                pass
count = 1
for s_url in urls:
    print("正在下载第" + str(count) + "页")
    get_video(s_url)
    count += 1

