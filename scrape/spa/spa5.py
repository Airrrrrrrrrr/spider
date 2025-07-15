"""
图书网站，无反爬，数据通过 Ajax 加载，有翻页，适合大批量动态页面渲染抓取。
"""
from DrissionPage import SessionPage

page = SessionPage()
for i in range(18, 90, 18):
    page.get(f'https://spa5.scrape.center/api/book/?limit=18&offset={i}')
    print(page.json)
