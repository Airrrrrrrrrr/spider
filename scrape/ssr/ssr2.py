# coding: utf-8
"""
无HTTPS证书，做HTTPS证书验证。
keyPoint: verify=False
"""

from DrissionPage import SessionPage

page = SessionPage()
page.get('https://ssr2.scrape.center/',verify=False)
print(page)
print(page.html)