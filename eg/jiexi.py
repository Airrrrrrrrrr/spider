import requests
import execjs
import time

def get_sign(link,timestamp):
    with open("jiexi.js", "r", encoding="utf-8") as f:
        js = execjs.compile(f.read())
        sign = js.call("g", link + str(timestamp))
        return sign
headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://www.yijianjiexi.com",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
cookies = {
    "__vtins__KPfVVEwb89cQ1LTN": "%7B%22sid%22%3A%20%221aedb5b7-7cfd-5cf8-ad7b-6e15ca30b76e%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201735621341467%2C%20%22ct%22%3A%201735619541467%7D",
    "__51uvsct__KPfVVEwb89cQ1LTN": "1",
    "__51vcke__KPfVVEwb89cQ1LTN": "bcf16140-55a4-57d3-b780-069f7c7e5210",
    "__51vuft__KPfVVEwb89cQ1LTN": "1735619541470",
    "login_key": "4152be58db9cff6954549f8d0dfa9bfd"
}
url = "http://www.yijianjiexi.com/api/web/getMaterial"
timestamp = int(time.time())
link = "https://www.bilibili.com/video/BV1p26VYnEhz/?share_source=copy_web&vd_source=d5ac5e7131ae4962ee3cf6489f342957"
s = get_sign(link, timestamp)
data = {
    "link": link,
    "t": timestamp,
    "s": s
}
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)
# print(response.status_code)
# print(response.text)
data = response.json()
print(data['data']['video_url'])
