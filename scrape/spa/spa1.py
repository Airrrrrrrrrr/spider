"""
无反爬，数据通过ajax加载，页面动态渲染
接口数据
"""
from DrissionPage import SessionPage
page = SessionPage()
for i in range(10, 100, 10):
    page.get(f'https://spa1.scrape.center/api/movie/?limit=10&offset={i}')
    print(page.json)
    