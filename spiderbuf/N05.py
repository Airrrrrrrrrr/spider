# 雪碧图反爬
# HTTP是基于TCP连接的，TCP连接的建立是需要时间和资源的。
# 而下载网页所需的图片资源是通过HTTP的。如果有非常多的小图片，就需要建立很多TCP连接。
# 勤劳勇敢的前端工作者们，想到把所有小图片放到一张图片里面去。
# 这样就可以通过一次TCP链接，下载所有的小图片，再通过前端的奇技淫巧，来展示正确的图片。
# 这种由很多小图片组成的图片，被称为雪碧图。雪碧图可以节约TCP连接的同时，也为爬取带来了难度。
# 因为，雪碧图是通过前端的奇技淫巧，来展示正确的图片，所以，爬虫无法直接获取到雪碧图。
# 但是，雪碧图可以通过分析雪碧图，来获取雪碧图包含的所有图片。

# 本次链接：https://spiderbuf.cn/playground/n05
# 相似案例（难度上升）：http://glidedsky.com/level/crawler-sprite-image-1
# 案例解决方法：https://blog.csdn.net/jia666666/article/details/109199875

from DrissionPage import SessionPage

page = SessionPage()
page.get('https://spiderbuf.cn/playground/n05')
num_class = page.eles('x://p/span')
for i in num_class:
    match i.attrs['class']:
        case 'sprite uvwxyz':
            print(3)
        case 'sprite cdefgh':
            print(9)
        case 'sprite abcdef':
            print(0)
        case 'sprite klmnop':
            print(6)
        case 'sprite mnopqr':
            print(2)
        case 'sprite yzabcd':
            print(4)
        case 'sprite wxyzab':
            print(8)
        case 'sprite efghij':
            print(5)


# 7296481530 雪碧图数字 背景图大小100px * 12px

# 思路1
# 经分析通过前端background-position属性，可以获取雪碧图包含的所有图片。background-position属性的值可以映射出数字值。
# 所以我们可以得出各个位置的数字。

# 思路2（这个思路仅能在类名不做变化的时候才可以）
# 类名和数字一一对应，做一个映射表。
# class_map = {
#     'sprite uvwxyz': 3,
#     'sprite cdefgh': 9,
#     'sprite abcdef': 0,
#     'sprite klmnop': 6,
#     'sprite mnopqr': 2,
#     'sprite yzabcd': 4,
#     'sprite wxyzab': 8,
#     'sprite efghij': 5
# }

# 思路3
# 参照解决方法