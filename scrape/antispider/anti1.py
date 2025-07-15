# -*- coding: utf-8 -*-
"""
对接 WebDriver 反爬，检测到使用 WebDriver 就不显示页面，适合用作 WebDriver 反爬练习。
"""
from DrissionPage import SessionPage

page = SessionPage()
titles = []
ranks = []
lengths = []
for i in range(1, 5):
    page.get(f'https://antispider1.scrape.center/api/movie/?limit=10&offset={ (i-1) * 10 }')
    print(page.json)