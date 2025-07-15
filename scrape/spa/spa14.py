"""
电影数据网站，数据通过 Ajax 加载，数据接口参数加密且有时间限制，加密过程通过数值型 WASM 实现，适合 WASM 逆向分析。
2024/12/3
"""
from DrissionPage import SessionPage
import subprocess
page = SessionPage()
sign = subprocess.run(['node', 'js/spa14_wasm.js'], stdout=subprocess.PIPE).stdout.decode()
print(sign)
url = f'https://spa14.scrape.center/api/movie?limit=10&offset=0&sign={sign}'
page.get(url)
print(page.html)