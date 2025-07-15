# 被屏蔽IP后使用代理服务器爬取页面

from DrissionPage import SessionPage, SessionOptions
from parsel import Selector
from fake_useragent import UserAgent

ua = UserAgent()
so = SessionOptions()
so.set_proxies('http://127.0.0.1:1080')  # 设置代理
so.set_headers(ua.random)  # 设置UA
page = SessionPage(session_or_options=so)
page.get('https://spiderbuf.cn/playground/e04')
selector = Selector(page.html)
href = selector.xpath('//ul[@class="pagination"]/li/a/@href').extract()
hrefs = ['https://spiderbuf.cn' + i for i in href]
print(len(hrefs[:-1]))
for i in hrefs[:-1]:
    page.get(i)
    selector = Selector(page.html)
    title = selector.xpath('//tr/td[3]/text()').extract()
    print(title)
