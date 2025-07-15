# current time:20241223 12点52分
"""
对接字体文件反爬，显示的内容并不在 HTML 内，而是隐藏在字体文件，设置了文字映射表，适合用作字体反爬练习。
伪元素反爬
"""
from DrissionPage import ChromiumPage, ChromiumOptions
from fake_useragent import UserAgent
import re
from parsel import Selector
# 保存操作，避免重复请求

# ua = UserAgent()
# co = ChromiumOptions()
# co.set_user_agent(ua.random)
# page = ChromiumPage(addr_or_opts=co)
# page.get('https://antispider4.scrape.center/')
# page.wait(3)
# html = page.html
# with open('anti4.html', 'w', encoding='utf-8') as f:
#     f.write(html)

# 获取字体文件，分析映射表
with open('anti4.css', 'r', encoding='utf-8') as f:
    css = f.read()
    pattern = re.compile('.icon-(.*?):before\{content:"(.*?)"\}')
    results = re.findall(pattern, css)
    icon_dict = {i[0]: i[1] for i in results}
    # print(icon_dict)

with open('anti4.html','r',encoding='utf-8') as f:
    html = f.read()
    sel = Selector(html)
    scores = []
    for i in range(1,11):
        styles = []
        style = sel.xpath(f'(//p[@class="score m-t-md m-b-n-sm"])[{i}]/span/i/@class').getall()
        for s in style:
            style = icon_dict[s.split('-')[1]]
            styles.append(style)
        scores.append(styles)
    print(scores)
    for nums in scores:
        num = nums[0]+nums[1]+nums[2]
        print(num)