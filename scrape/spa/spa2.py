"""
电影数据网站，无反爬，数据通过 Ajax 加载，数据接口参数加密且有时间限制，适合动态页面渲染爬取或 JavaScript 逆向分析。
扣代码

"""
import subprocess
from DrissionPage import SessionPage

page = SessionPage()
limit = 10
num = 2 # 需要去spa2.js中修改getToken的参数并同步。
token = subprocess.run(['node', 'scrape/spa/js/spa2.js'], stdout=subprocess.PIPE).stdout.decode()
url = f'https://spa2.scrape.center/api/movie?limit={limit}&offset={(num - 1) * limit}&token={token}'
page.get(url)
print(page.html)


# 循环获取数据需要能对js中的代码进行传参，暂未实现。
# for num in range(1, 6):
#
#     token = subprocess.run(['node', 'spa2.js'], stdout=subprocess.PIPE).stdout.decode()
#     url = f'https://spa2.scrape.center/api/movie?limit={limit}&offset={(num - 1) * limit}&token={token}'
#     page.get(url)
#     print(page.html)