'''
time: 2024/12/26
ob混淆
动态cooike加载
MD5魔改
数据通过api接口获取
'''

from DrissionPage import SessionPage, SessionOptions
from fake_useragent import UserAgent
import subprocess

ua = UserAgent()

m = subprocess.run(['node', 'yrx_2.js'], stdout=subprocess.PIPE).stdout.decode().strip().replace('\n', '')
print(m)
so = SessionOptions()
cookies = ['sessionid=smtjioxamgj526t094lp9n71bbd37jkf',f'm={m};']
so.set_a_header('UserAgent', ua.random)
so.set_cookies(cookies)
page = SessionPage(session_or_options=so)
result = 0
for i in range(1, 6):
    page.get(f'https://match.yuanrenxue.cn/api/match/2?page={i}')
    values = page.json['data']
    for value in values:
        result += value['value']
print(result)

