# -*- coding: utf-8 -*-
"""
对接 User-Agent 反爬，检测到常见爬虫 User-Agent 就会拒绝响应，适合用作 User-Agent 反爬练习。

"""
from DrissionPage import SessionPage, SessionOptions, ChromiumPage
from fake_useragent import UserAgent
from parsel import Selector
import re
from pandas import DataFrame
def dataByInterface():
    '''
    这个网站有接口可以直接拿数据，不用模拟浏览器。
    :return:
    '''
    ua = UserAgent()

    so = SessionOptions()

    for i in range(1, 5):
        so.headers['User-Agent'] = ua.random
        page = SessionPage(session_or_options=so)
        page.get(f'https://antispider3.scrape.center/api/book/?limit=18&offset={18 * (i - 1)}')
        print(page.json)



def dataByBrowser():
    '''
    模拟浏览器的做法:
    模拟浏览器，获取渲染后的页面。
    页面中的文字是通过css的样式排列的，所以我们正常浏览的时候是没有影响的。
    但是在调试的时候看起来文字就是被打乱的，所以我们需要根据样式来还原文字。
    这里发现文字偏移是通过style="left: 16*n px;"的样式来定位的。
    我们只需要获取所有的style，然后根据偏移量还原文字。
    :return:
    '''

    page = ChromiumPage(9333)
    page.get('https://antispider3.scrape.center/page/2')
    page.wait(3)  # 等待浏览器渲染页面
    html = page.html
    print(html)
    # 保存一份做测试
    with open('page.html', 'w', encoding='utf-8') as f:
        f.write(html)
def parse():
    '''
    解析数据
    :return:
    '''
    with open('page.html', 'r', encoding='utf-8') as f:
        html = f.read()
        sel = Selector(html)
        names = []
        for i in range(1,19):
            a_name = sel.xpath(f'(//h3)[{i}]/span/@style').getall()
            if a_name:
                c_name = []
                nums = []
                for a in a_name:
                    num = re.findall('\d+', a)
                    nums.extend(num)
                for n in nums:
                    name = sel.xpath(f'(//h3)[{i}]/span[{int(n) /16 + 1}]/text()').get()
                    name = name.strip().replace('\n', '')
                    c_name.append(name)
                c_name = ''.join(c_name)
                names.append(c_name)
                # print(nums)
            else:
                b_name = sel.xpath(f'(//h3)[{i}]/text()').get()
                names.append(b_name)



        authors = sel.xpath('//p[@class="authors"]/text()').getall()
        authors = [a.strip().replace('\n', '') for a in authors]
        authors.append(authors[16])
        authors[16] = ''
        covers = sel.xpath('//img[@class="cover"]/@src').getall()
        print(len(names),len(authors),len(covers))
        df = DataFrame({'names': names, 'authors': authors, 'covers': covers})
        df.to_excel('data.xlsx', index=False)
        print(names)
        print(authors)
        print(covers)

if __name__ == '__main__':
    parse()