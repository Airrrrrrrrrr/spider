import requests
from hashlib import md5
import time
import re
def get_sign(page):
    timestamp1 = str(int(time.time() * 1000))
    md5_sign = md5(f'{page}|{timestamp1}D#uqGdcw41pWeNXm'.encode()).hexdigest()
    return page,md5_sign,timestamp1
headers = {
    'authority': 'match.yuanrenxue.cn',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://match.yuanrenxue.cn/match/20',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1732179877; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1732799435; HMACCOUNT=5AE2446D329365CD; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1732799435; tk=1980960723265784687; sessionid=val753raqc7lp6u8syefylcazigawqop; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1732799447; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1732799511',
}
results = []
for i in range(1,6):
    page,sign,t = get_sign(i)
    params = (
        ('page', page),
        ('sign', sign),
        ('t', t),
    )

    response = requests.get('https://match.yuanrenxue.cn/api/match/20', headers=headers, params=params)
    text = response.text
    result = re.findall(r'"value": (\d+)', text)
    results.extend(result)
sums = sum(map(int, results))
print(sums)

