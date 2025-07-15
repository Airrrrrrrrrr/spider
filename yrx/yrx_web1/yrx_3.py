import array
import numpy as np
import requests

session = requests.Session()
session.headers = {
    'Content-Length': '0',
    'Accept': '*/*',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    "Cookie": "sessionid=9it2btsqqe7ueicul4juh14picbjc4sl"
}
cookies = {
    "sessionid": "9it2btsqqe7ueicul4juh14picbjc4sl",
    "qpfccr": "true",
    "no-alert3": "true",
    "m": "12c947b4841d9841a6abdd90cc7bef02|1749712826000"
}

a = []
b = []
print(1)
for i in range(1, 6):
    session.post('https://match.yuanrenxue.cn/jssm')
    data = session.get(f'https://match.yuanrenxue.com/api/match/3?page={i}').json()
    values = data['data']

    for n in range(len(values)):
        if values[n]['value'] not in a:
            a.append(values[n]['value'])
            b.append(1)
        else:
            b[a.index(values[n]['value'])] += 1
print(a)
print(b)
print(2)
