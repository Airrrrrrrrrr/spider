# -*- coding: utf-8 -*-
"""
无反爬措施
爬取电影基本信息
"""
from DrissionPage import SessionPage

page = SessionPage()
titles = []
ranks = []
lengths = []
for i in range(1, 5):
    page.get(f'https://ssr1.scrape.center/page/{i}')
    title = page.eles('x://h2/text()')
    rank = page.eles('x://p[@class="score m-t-md m-b-n-sm"]/text()')
    length = page.eles('x://div[@class="m-v-sm info"]/span[3]/text()')
    titles.extend(title)
    ranks.extend(rank)
    lengths.extend(length)

for i in range(len(titles)):
    print(f'{titles[i]} {ranks[i]} {lengths[i]}')
