# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:01:05 2020
伪元素反爬
利用CSS的伪元素::before和::after来插入额外的内容到HTML文档中，这些内容实际上并不直接存在于HTML源代码里，而是通过浏览器渲染时由CSS动态添加的。
"""


from DrissionPage import SessionPage


# 创建一个字典来存储映射
css_content_mapping = {
    'abcdef': ('7', '5'),
    'ghijkl': ('8', '9'),
    'mnopqr': ('9', '1'),
    'uvwxyz': ('1', '4'),
    'yzabcd': ('2', '6'),
    'efghij': ('3', '2'),
    'klmnop': ('5', '7'),
    'qrstuv': ('4', '3'),
    'wxyzab': ('6', '0'),
    'cdefgh': ('0', '8'),
    # 以下类只定义了::after，所以::before设置为None
    'hijklm': (None, '6'),
    'opqrst': (None, '0'),
    'uvwxab': (None, '3'),
    'cdijkl': (None, '8'),
    'pqrmno': (None, '1'),
    'stuvwx': (None, '4'),
    'pkenmc': (None, '7'),
    'tcwdsk': (None, '9'),
    'mkrtyu': (None, '5'),
    'umdrtk': (None, '2')
}
rank_list = []

page = SessionPage()
page.get('https://spiderbuf.cn/playground/n04')
ranks = page.eles('x://div[@class="col-xs-9 col-lg-9"]/span[2]')

for rank in ranks:
     class_name = rank.attrs['class'].split(' ')
     first_grade = css_content_mapping[class_name[0]][0]
     second_grade = css_content_mapping[class_name[1]][1]
     print(first_grade, second_grade)
     rank_list.append(first_grade + '.' + second_grade)

print(rank_list)
