"""
登录验证，无验证码
在登录界面进行抓包，header中有Authorization认证
请求时header中带入登录后的Authorization即可。
"""
from DrissionPage import SessionPage,SessionOptions

so = SessionOptions()
so.set_a_header('Authorization','Basic YWRtaW46YWRtaW4=')

page = SessionPage(session_or_options=so)
page.get('https://ssr3.scrape.center/')
print(page.html)
