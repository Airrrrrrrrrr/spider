"""
对接 Session + Cookies 模拟登录，适合用作 Session + Cookies 模拟登录练习。
"""
from DrissionPage import SessionPage, SessionOptions, ChromiumPage, ChromiumOptions
so = SessionOptions()
co = ChromiumOptions().new_env()  # 创建全新浏览器对象

'''
不适用于短时效的cookies

核心思路如下：
1.自动化执行登录操作（扫码或表单填写）
2.登录成功后记录cookies到本地
3.携带记录好的cookies使用sessionpage进行请求网页获取数据
4.如果cookies过期，重复执行前3步操作

cookies、session、JWT三种登录携带的参数都会有过期时间，看网站开发人员设置的期限。
'''



# 新建文件本地读取cookies，r+ : 可读、可写，文件不存在也会报错，写操作时会覆盖
# 所以自己先新建一个cookies文件，文件名为mycookies.txt
with open('mycookies.txt', 'r+', encoding='utf-8') as f:
    flag = f.read()
    if flag != '':      # 检测cookies文件是否为空，不为空读取cookies并设置，直接请求
        page = ChromiumPage()
        page.set.cookies(flag)
        page.get('https://www.17k.com/')
    else:       # cookies文件为空，则使用浏览器模拟登录，并保存cookies到文件
        page = ChromiumPage(co)
        tab = page.new_tab()
        tab.get('https://www.17k.com/')
        # 模拟登录
        # 填表单并点击登录按钮
        # 或者做扫码操作
        username = tab.eles('x:(//input)')[0]
        password = tab.eles('x:(//input)')[1]
        submit = tab.eles('x:(//input)')[2]
        username.input('admin')
        password.input('admin')
        submit.click()
        tab.wait(3)
        # 获取cookies，处理后保存到文件
        c = tab.cookies() # 这里返回的是一个列表，需要对其进行处理 [{'name': 'sessionid', 'value': 'bgjwc6n7sw5rfnqvt14bm0tm1pmvtmwh', 'domain': 'login2.scrape.center'}]
        cookies = c[0]["name"] + '=' + c[0]["value"] + ';'
        print(cookies)
        f.write(cookies)
