import requests
from config import LEETCODE

s = requests.session()

headers_base = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'leetcode.com',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
    'Referer': 'https://leetcode.com/accounts/login/',
}
login_data = {}

def login():
    url = "https://leetcode.com/accounts/login/"
    res = s.get(url=url, headers=headers_base)
    print(res.cookies['csrftoken'])
    login_data['csrfmiddlewaretoken'] = res.cookies['csrftoken']
    login_data['login'] = LEETCODE['username']
    login_data['password'] = LEETCODE['password']
    res = s.post(url, headers=headers_base, data=login_data)
    print(res.status_code)
    return res.cookies


if __name__ == "__main__":
    login()