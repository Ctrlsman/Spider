import requests
from bs4 import BeautifulSoup

result = requests.get("https://github.com/login")
soup = BeautifulSoup(result.text, 'html.parser')
token = soup.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
r1_cookie_dict = result.cookies.get_dict()
r2 = requests.post(
    "https://github.com/session",
    data={
        "utf8": '✓',
        'authenticity_token': token,
        'login': 'your username',
        'password': 'your password',
        'commit': 'Sign in'
    },
    cookies=r1_cookie_dict
)

r2_cookies_dict = r2.cookies.get_dict()
cookie_dict = {}
cookie_dict.update(r1_cookie_dict)
cookie_dict.update(r2_cookies_dict)

r3 = requests.get('https://github.com/settings/emails',
                  cookies=cookie_dict)
print(r3.text)
# 最后检查一下发现登录信息了
