import traceback
import json
import requests
import execjs


def get_data(page, all_params):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/5",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "sessionid": "n2cveyxk7a8w5dlwfqs11dxgszd960q6",
        "no-alert3": "true",
        "m": all_params['cookie']['m'],
        "RM4hZBv0dDon443M": all_params['cookie']['RM4'],
    }
    m = all_params['params']['m']
    f = all_params['params']['f']
    url = f"https://match.yuanrenxue.cn/api/match/5?page={page}&m={m}&f={f}"


    response = requests.get(url, headers=headers, cookies=cookies)
    print(response)
    data = response.json()
    print(data)
    return data

def get_data1(page, all_params):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/5",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies = {
        "sessionid": "n2cveyxk7a8w5dlwfqs11dxgszd960q6",
        "no-alert3": "true",
        "m": all_params['cookie_m'],
        "RM4hZBv0dDon443M": all_params['cookie_rm4'],
    }
    m = all_params['m']
    f = all_params['f']
    url = f"https://match.yuanrenxue.cn/api/match/5?page={page}&m={m}&f={f}"


    response = requests.get(url, headers=headers, cookies=cookies)
    data = response.json()
    print(data)
    return data

value_list = []

# with open('yrx_5.js', 'r', encoding='utf-8') as f:
#     jscode = execjs.compile(f.read())
# all_params = jscode.call('get_cookie')
# for i in range(1, 6):
#     values = get_data(page=i, all_params=all_params)
#     for value in values['data']:
#         value_list.append(value['value'])

with open('yrx_5_2.js', 'r', encoding='utf-8') as f:
    jscode = execjs.compile(f.read())
all_params = jscode.call('getParamers')
for i in range(1, 6):
    values = get_data1(page=i, all_params=all_params)
    for value in values['data']:
        value_list.append(value['value'])



value_list.sort()
print(value_list)
nums = value_list[-5::]
print(nums)
sum = 0
for a in nums:
    sum += a
print(sum)