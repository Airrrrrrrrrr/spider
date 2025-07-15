'''
time: 2025年6月11日
ob混淆

'''
import base64
import requests
import execjs
import time

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/1",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# 读取JS文件并编译
with open('yrx_1.js', 'r') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
m = ctx.call("generateM")

def po(page, m):
    url = "https://match.yuanrenxue.cn/api/match/1"
    params = {
        "page": str(page),
        "m": m
    }
    response = requests.get(url, headers=headers,  params=params)
    print(f"Page {page} response:", response.text)

# 每次请求生成新的m参数
for i in range(1, 2):
    # 调用JS函数生成m参数
    po(i, m)
    time.sleep(0.1)  # 避免请求过快