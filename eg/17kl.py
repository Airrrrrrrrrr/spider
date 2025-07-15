import os
import traceback
from DrissionPage import Chromium,ChromiumOptions
co = ChromiumOptions().new_env()
# 定义保存 cookies 的文件名
COOKIES_FILE = "mycookies.txt"
# c = "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22103990284%22%2C%22%24device_id%22%3A%22194dc0d14f2172d-0e1813e7acc9e1-26011b51-1821369-194dc0d14f3213f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%224c6e406b-911d-4ceb-bea4-aeab1ce7ad2b%22%7D; ssxmod_itna2=Qq0xyD2D0DRDnDRrxxz2DUAUQ3RWYDfgD2onjqA6WPD/bxKuP7=D2WeD; Hm_lpvt_9793f42b498361373512340937deb2a0=1738858715; _openId=ow-yN5k35b9dAve_UUiO44jjtgAQ; Hm_lvt_9793f42b498361373512340937deb2a0=1738858632,1738858653,1738858701; tfstk=ggLZasGbZV3aw6LZn6b4z4d4IE_OkNDSQE6fiIAc1OXGlcBcnIpdGrOcjJDVLKB1fNvX3-J6dOv2MfCcnKvVhhiIPCdOkZD534gW6BC4GDJNm12nisf8nXsi1InlfZDSF2_B6msGodToy6eet9CVitXMnWcFgs_0Si4gxJXdiZbcjr2Ht_1GsRXgjXRhpsbcnKbmpXp9H81ljjDlH5pSqsjNECXUzBLFswZ9_9r8Ve-FbTbVLr4D81RIoccYzm6k2Os5Yp0Q7ZRhgd6BE44F-g-JGsJZ7Pb6xHLO5eMzwGJVCgYCY22FTeRWq6dE4XReuOSkSMPbyCQNiKj2vYz5_NtF4F-tMJAMFO-lWINrCBSyYgChxSrG53OWkgYi78BC2sJ1dL0u8wjc4keAtAKJkhy0mGfdTTGETU7Sal9IdxW3DoIhq6WS6iqYDGfPTTGEwoEAXuCFFfkA.; HMACCOUNT=E8226E60968DF27B; ssxmod_itna=Qq0xyD2D0DRDnDRrxxz2DUAUQ3RWYDfgD2onjLqGNmi3DZDiqAPGhDC+89hi2fom+ihWPCi5q3Q0bxDkFU7iTabIUGoP5WDCPGnDB9DtY8bxiiyDCeDIDWeDiDGR=DFxYoDeOyQDFzHNXZzd=D3qDwDB=DmqG2Yl=Dm4DfDDLyK0oPzk=D4qDBDGteZCiDG4GfmTxD0TxHxfoPDYpy0LdPomri5DNeiB=DjqGgDBLiYFTNd/7PlqNzZaFabqrexBQD7MrM/+2dmqiZQTFdCip5A05KYG4+i7DeYD45Wi3677Dotrjxt4xYziiGidQi3l2xdcxMGDD===; c_csc=web; accessToken=nickname%3D%25E7%25BA%25AA%25E4%25B8%258D%25E4%25BD%258F255536392%26avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F04%252F84%252F02%252F103990284.jpg-88x88%253Fv%253D1738848415000%26id%3D103990284%26e%3D1754410714%26s%3D8d9432c3ff1ee320; acw_tc=1a0c650a17388586320812592e003a4801be5fc3e14c59a290c5e672dcdefd; c_channel=0; sajssdk_2015_cross_new_user=1; acw_sc__v2=67a4e0883ba2f0b73ab81cfd6eb1691ab6a63e71; GUID=4c6e406b-911d-4ceb-bea4-aeab1ce7ad2b"
# 判断是否存在已保存的 cookies 文件
if os.path.exists(COOKIES_FILE)and os.path.getsize(COOKIES_FILE)> 0:
    try:
        # 如果存在且不为空，则加载 cookies
        with open(COOKIES_FILE,"r+",encoding="utf-8") as f:
            flag = f.read()
            """自动登录成功后点击书架"""
            page = Chromium(co)
            page.set.cookies(flag)
            tab = page.new_tab('https://www.17k.com/')
            tab.ele('书架').click()
    except Exception as e:
        traceback.print_exc()
        #如果加载失败，删除无效的 cookies 文件
        os.remove(COOKIES_FILE)
        with open(COOKIES_FILE, "w", encoding="utf-8") as f:
            f.write("")
        print("已删除无效的 cookies 文件")
else:
    page = Chromium()
    tab = page.new_tab('https://www.17k.com/')
    tab.ele('登录').click()
    weixin = tab.ele('x://img[@alt="微信登录"]')
    weixin.click()
    tab.wait.url_change('https://www.17k.com/?code=1')
    with open(COOKIES_FILE, "r+", encoding="utf-8") as f:
        cookies = tab.cookies().as_str() + "; domain=.17k.com"
        f.write(cookies)
    tab.ele('书架').click()

