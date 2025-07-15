# -*- coding: utf-8 -*-
"""
对接 User-Agent 反爬，检测到常见爬虫 User-Agent 就会拒绝响应，适合用作 User-Agent 反爬练习。
"""
from DrissionPage import SessionPage, SessionOptions
from fake_useragent import UserAgent
ua = UserAgent()
so = SessionOptions()



titles = []
ranks = []
lengths = []
for i in range(1, 5):
    so.headers['User-Agent'] = ua.random
    page = SessionPage(session_or_options=so)
    page.get(f'https://antispider2.scrape.center/page/{i}')
    title = page.eles('x://h2/text()')
    rank = page.eles('x://p[@class="score m-t-md m-b-n-sm"]/text()')
    length = page.eles('x://div[@class="m-v-sm info"]/span[3]/text()')
    titles.extend(title)
    ranks.extend(rank)
    lengths.extend(length)

for i in range(len(titles)):
    print(f'{titles[i]} {ranks[i]} {lengths[i]}')

print('end')