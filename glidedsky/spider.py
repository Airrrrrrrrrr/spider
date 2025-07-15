from DrissionPage import ChromiumPage
from parsel import Selector
page = ChromiumPage(9333)
# page.get('http://www.glidedsky.com/level/web/crawler-basic-1')
# print(page.html)
text = page.html
selector = Selector(text)
nums = selector.xpath('//div[@class="col-md-1"]/text()').extract()
reslut = sum([int(i) for i in nums])
print(reslut)