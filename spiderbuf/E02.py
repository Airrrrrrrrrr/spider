# coding=utf-8
"""
简单的验证码登录。
带cookies的登录验证。
"""
import requests
from lxml import etree

url = 'https://spiderbuf.cn/playground/e02/list'

myheaders =  {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://spiderbuf.cn/playground/e02",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "__gads": "ID=5c6b2f639121f44b:T=1732863435:RT=1733064734:S=ALNI_MY-3rIXhDQn9oy2jJPcv9KxyocwDg",
    "__gpi": "UID=00000fa2576fdbd3:T=1732863435:RT=1733064734:S=ALNI_MZexWTtB8OPVAF7etOFNwxQNTCJ2Q",
    "__eoi": "ID=eee678f168d75e86:T=1732863435:RT=1733064734:S=AA-AfjbcFbAJXLAWBNN-1lUSTTfO",
    "admin": "a19dc154b5648e223baa6282f0ba657"
}

payload = {'username':'admin','password':'123456'}

html = requests.get(url, headers=myheaders,cookies=cookies).text
print(html)

f = open('e02.html', 'w', encoding='utf-8')
f.write(html)
f.close()

root = etree.HTML(html)
trs = root.xpath('//tr')

f = open('data_e02.txt', 'w', encoding='utf-8')
for tr in trs:
    tds = tr.xpath('./td')
    s = ''
    for td in tds:
        # print(td.text)
        s = s + str(td.text) + '|'
    print(s)
    if s != '':
        f.write(s + '\n')

f.close()
