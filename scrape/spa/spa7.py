"""
NBA 球星数据网站，数据纯前端渲染，Token 经过加密处理，适合基础 JavaScript 模拟分析。
"""
from DrissionPage import SessionPage
page = SessionPage()
page.get('https://spa7.scrape.center/js/main.js')
print(page.html)