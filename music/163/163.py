'''
网易云音乐params和encSecKey参数
aes和rsa加密
'''

import requests
import subprocess

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.163.com/discover/toplist?id=3778678",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
cookies = {
    "JSESSIONID-WYYY": "8BBVql0zQvU2X8jW9xZCCYcnW%5CDKo9zDSGKPqOeRgWPyNs84%2Fl2O%2BRV1p9UjInj%2BoQFVvw4zU4M%5CMndnExmYQZKsUf6SZobAJXBvaYS2vPY6jrukDkcd%5CDyBWtGjsZbjBHsxBvDiMazaT5eCa4C86%2FREyKJDPuhWxoBBeJbH%5Cn743Ub2%3A1751429525421",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "b5722168dcecdf8c690ae4fa8f474b7f,1751427725439",
    "_ntes_nuid": "b5722168dcecdf8c690ae4fa8f474b7f",
    "WEVNSM": "1.0.0",
    "WNMCID": "ldckpf.1751427725708.01.0",
    "WM_NI": "0SPavGRTRu%2B2%2FTXmKia2IYKG0EQ4B8yL1aZtHkdTwA%2BvVhXCYq6c8IaSZapASjyk6vNQMdxplpNlNhGvErzPne4FMlYwT%2BFDVrBFdzoe%2FxCC3NwS%2FCmhPITPbvTQjznWU2E%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eeb9d65cf8998c86b24ff19a8ab7d54e968e9a86c66eb2898ca8b83bf1869da5ec2af0fea7c3b92af48da082f54d928c9e96aa3aed8c988eca63a3ee87baca4df49b9fd5c134bb94ff82d9808cb5acb5f64be9aa9a89db499baffa84bb43a38d9682f34b91b6b78cb57e8e8f8385fb7cb0b0828dcd6485aa8b93f95caebbfca7d0689ba99cccc55096ae8ea7e772adbbe199c249f192b9b4ae49afb8a0aad75ca2aa9cb2e972ae899bd3c837e2a3",
    "WM_TID": "6tjswxN4wLhAFEBQEFPSe6CSH5hjJXWj",
    "NMTID": "00OQmQS2-G8sHu1MUODvWyDyo6pD2wAAAGXyTq72Q",
    "__snaker__id": "MddSWCtlTTLPLLNV",
    "gdxidpyhxdE": "sVN3r7mDivPP%2BmmBHl%2BEucn3WDLsDI%2FKf%5Cyxyf3loWIH9MZadMAs%5CtAt8P3aQWgnPA0SA6QETkefx%2BtmNylq37ipBYG7HUAd0xbV%2FvAcDBriWuC%2Byhr5c1fm3XWmKaEVb%2BO27Xjyc5szIHNOPU8UURcVzvS%5CAQlrDH9neCJZhQdNJlnS%3A1751428879314"
}
url = "https://music.163.com/weapi/comment/resource/comments/get"
params = {
    "csrf_token": ""
}
process = subprocess.run(['node', '163.js'],
                         capture_output=True,
                         text=True,
                         encoding='utf-8',)
output = process.stdout
print(output)

data = {
    "params": "B31AyFC/F9tHQMoUHggvy4Pv4OwwR65pt/WLO3eh4cKlhYSJzs/B3JM5z6InQes97ltjsudzGtz3Bu2ijab+u5gbbbgs12ZCxtR4aj3nJIbUXHaTq01J/7Pajqo9DqVlFhwuxkkFFbg4h2kTyMVxcFERaiCG8+dT6ue6pVHHp7xYqX48FSeRtK57z9PLctv3Owz1fGUr5D80vhCnesFVXMLEwTXi6TWlsMUmTm9YyLsQGqE82CPB1hxFVQHXrx8u8QpBXaqyZJjfbgEf8ajQAA==",
    "encSecKey": "8047689db3ec2d76887fbccf30f6adf15968b42515ca8f3132f315f660979b4e6dbcee5932e0324fb2c8adf3c41b701d2e3394d558337e77c20ad95010a65c51c333600cc4d453d3952fc4c0133cb199da971ad294b9fe20b45a192b88ee52c1613ec61f9f060639b652ae8499c9c9dec56988a4b8378619d7baa2ec1d5a0134"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.json())
print(response)