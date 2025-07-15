# import requests
'''
东航手机web端，refer__1036参数。
'''
from curl_cffi import requests
import json
import subprocess
from urllib.parse import quote

def call_js_function(params=None):
    """调用JS函数，根据参数执行不同操作"""
    # 准备参数（无参数时传空字典）
    js_params = params or {}

    # 通过Node.js执行
    process = subprocess.run(
        ['node', 'm_ceair.js', json.dumps(js_params)],
        capture_output=True,
        text=True,
        encoding='utf-8',
    )

    # 解析结果
    try:
        output = json.loads(process.stdout)
        if output['success']:
            return output['data']
        else:
            raise Exception(f"JS执行错误: {output['error']}")
    except json.JSONDecodeError:
        raise Exception(f"无效的JS输出: {process.stdout}")

myObj = call_js_function()
refer__1036 = myObj["refer__1036"]
refer__1036 = quote(refer__1036)


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "M-CEAIR-ENCRYPTED": "true",
    "Origin": "https://m.ceair.com",
    "Pragma": "no-cache",
    "Referer": "https://m.ceair.com/mapp/reserve/flightList?newParam=%7B%22tripType%22%3A0,%22depCode%22%3A%22SIA%22,%22arrCode%22%3A%22UYN%22,%22dt%22%3A%221%22,%22at%22%3A%221%22,%22depN%22%3A%22%E8%A5%BF%E5%AE%89%22,%22arrN%22%3A%22%E6%A6%86%E6%9E%97%22,%22flightDate%22%3A%2220250624%22,%22carryChd%22%3Afalse,%22carryInf%22%3Afalse,%22productType%22%3A%22CASH%22,%22curIndex%22%3A0,%22memberLabel%22%3A%22%22,%22zoneCode%22%3A%22STRANGE_SHOPPING%22,%22isTax%22%3Afalse,%22interTax%22%3Atrue%7D&yjr_common_code=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36 Edg/138.0.0.0",
    "X-CEAIR-OS": "M",
    "X-Tingyun": myObj['X-Tingyun'],
    "ceair-token;": "",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "transactionId": myObj["Transactionid"],
}
cookies = {
    "language": "zh_CN",
    "_c_WBKFRo": "EWwLsOYRLpnC0saBnxY0IPY3BN2VHP1yaFTmCz2c",
    "acw_tc": "0aef816617513461283845355e0076b27c9e8ea89caf770bd8dcc2ad6d262b",
    "SERVERID": "7c6d891e1ad776fa817774b54370c884|1751346318|1751346129",
    "ssxmod_itna": "Yq+xyiD=KWq7qhx4wDR2WpKqAQ=50dGMBDeq7tDRDFqApxDHDIx9YPlGhitx+xDvsqmxbFqCDBd4YDSxD6FDK4GTG8pB5D70g0iF1SWtDqxCz=AQkHmo7GUb44YutHEy3E1GViFneR8rrGD0aDmKDUouDCx4Dx=PD5xDTDWeDGDD3TxGaDmeDecOwD0+pC4fAF4o5D7eDXxGCDQK5F4GWDiPD7OEQfpppb3xD0xD1UtjfDDPDapOFDGHFTvcDNmPDE7gvP4d5RFjQsbDxF4G1vD0HQmt0qLtMOaSv+Tt9YxELU40OD0F61SiR4KOSWhfr7qeqYxYOhG7dqB5GGx3rKeB50odR0xoDe02xZhxRGx1mDt0YwoxZAmG0xBBhGiOBDiBAQ1QtUQslMsF3Gqeebn8chte6YK7DGlxVDqG0DbQ5MA5DoxrmxTj4aGw5pxd4+aiDD",
    "ssxmod_itna2": "Yq+xyiD=KWq7qhx4wDR2WpKqAQ=50dGMBDeq7tDRDFqApxDHDIx9YPlGhitx+xDvsqmxbFqiDG4nweP5DDKDLii2n1NwDGXFDwIYfjvkpZkSD0+kZaFW5RR/pxSjbNNBtZAb1mYNhEN=iFprP7tmPWr1yCvahhOZ5kRWrzb/KHrO0C6iAmEr7Oh6amr3FmLpImtjECqefGXQaAE1Fa+3PxvowGefEAPF0CPK2Ce3pAjZvqQjcffxKjgKadt3qxw3Hd/I9tTX9h60FjW2MnSz6w2/LW6egkbsjEv1lkshdFO2IWoC6/zZUzj+xGnN75xCicz+xUTszhuKGXUFM/RdmwA8HO4vvKuO4HEBBntBIKGuicAnn28BH/qxz4p0paeuH4aVjRCnWy/a6t9cegfiF1Iwq3ujimw4bkmxuWwBbGoOfynafRBUKExy9A7y8UmZDupnmUUWa8vaZ9ItGg9mu+nhtIHm7ClSF/R8eeQuas48Pzuff9NGWL97a=4w7wTpMsfPKKaYEL7Q7ktedTYm/u43IH381/EQ=q7fEpsuljRsVqOhDm0PFkgWj7=6Bwq7xm7OnPjf=n9bLKgW/js+4qzwWmRqFRNf0N0r+=0fbGQ7wqKYLh7uszIfj+7/VnHfaeovRhqTPzb4Qa+VU4CCyXufbX+0tMxXZS/uNwTTIr36MjXuxTEE5V21PbZgPZ5xD4NhkjxXmPi55Dp7xKDYneNx444KiRpqMiNDeoGL0DF7Pz5GixQhRGDD"
}

url = f"https://m.ceair.com/m-base/sale/shoppingv2?refer__1036={refer__1036}"
data = {
    "req": myObj["req"],
}
data = json.dumps(data, separators=(',', ':'))

response = requests.post(url, headers=headers, data=data,cookies=cookies)
data = response.json()
res = data["res"]

decrypt_params = {
    "avg1": res,
}
decrypted = call_js_function(decrypt_params)
print("解密结果:", decrypted)



