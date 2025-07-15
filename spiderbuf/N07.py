# 随机CSS样式类名，无Element ID
from DrissionPage import SessionPage
from parsel import Selector
page = SessionPage()
page.get('https://spiderbuf.cn/playground/n07')
selector = Selector(page.html)
title = selector.xpath('//div[@class="aQCrMS"]/text()').extract()
print(title)
name = selector.xpath('//div[@class="mMLcxC"]/text()').extract()
print(name)