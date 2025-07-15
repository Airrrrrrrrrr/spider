"""
顶象滑块
ac参数逆向
time：2025年7月14日
"""

import cv2
import random
import requests
from PIL import Image
from loguru import logger
from tools.time_tools.timestamp_tool import timestamp_by_num

pic_base_url = 'https://static4.dingxiang-inc.com/picture'

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "If-None-Match": "6874721eFZXJd3RyCypk0NU5JKuWeqkAMnLF43i1",
    "Origin": "https://www.dingxiang-inc.com",
    "Param": "5012#X8XIEJlsqnjcMBNvK5GeXrm8RtZisr2NuPvYJVnr1PQiiMc58PcUHycBhdZY4Mnz8t/hn38ATtIhvMfEuDWasmyo1DVksM7bTDIhWVvVTzvjnC/z3YyWH/TNTd8DW/u281njXXp9Nkj/rFAvGIGVM88XILEiCfuGCjC8U3MUR/xZh34GDPmpfPxv+nbOL5+mTATehNmCEN9GC5uDf5TED3xvHVW5m8Xeo+66cyRcvG3wohIL9J/L5lDaS06t2pnLXg6t2eDY5pnR9hFYoQDc9Wsuo8==",
    "Pragma": "no-cache",
    "Referer": "https://www.dingxiang-inc.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
}

def request1():
    """
    时间戳请求
    """
    url = "https://constid.dingxiang-inc.com/udid/c1"
    params = {
        "_t": str(timestamp_by_num(13))[-5:]
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.text)

def request2():
    """
    获取sid和图片
    """
    url = "https://cap.dingxiang-inc.com/api/a"
    aid = 'dx-' + str(timestamp_by_num(13)) + '-' + '3'
    params = {
        "w": "380", # 定值
        "h": "165", # 定值
        "s": "50", # 定值
        "ak": "99de95ad1f23597c23b3558d932ded3c", # 定值
        "c": "6874721eFZXJd3RyCypk0NU5JKuWeqkAMnLF43i1", # 定值
        "jsv": "5.1.53", # 定值
        "aid": aid, # 好像不校验
        "wp": "1", # 定值
        "de": "0", # 定值
        "uid": "", # 定值
        "lf": "0", # 定值
        "tpc": "", # 定值
        "t": "5552EBC77E7849742BF1C79BD44F27629A627D730A0FDB069F181963CF4EA7068573CB600D4B62C79714D64C740F5AD492D0DFFDA4CCDB652D06F7CEF5E02A5E61DE0030510441B5B82B01CAE5F0B9E7", # 定值
        "cid": "00173760", # 定值
        "_r": "0.2796900394082077" # 随机数好像不校验
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    sid = data['sid']
    p1 = data['p1']
    p2 = data['p2']
    return sid, p1, p2, aid

def download_captcha(bg, slice):
    """
    下载传回的图片，为后续计算滑动距离轨迹做铺垫。
    """
    response = requests.get(pic_base_url+bg, headers=headers)
    with open("captcha_bg.jpg", "wb") as f:
        f.write(response.content)

    response = requests.get(pic_base_url+slice, headers=headers)
    with open("captcha_slice.jpg", "wb") as f:
        f.write(response.content)
    logger.info("已下载图片!")

def parse_captcha(array,img):
    """
    还原底图
    """
    source_img = Image.open(img)
    output_img = Image.new("RGB", (384, 200))  # 32块 x 12像素 = 384宽度
    c = array
    p = 32
    for l in range(p):
        n = c[l]
        r = n * 12
        # 从源图像裁剪12x200的区域，粘贴到目标位置
        tile = source_img.crop((r, 0, r + 12, 200))
        output_img.paste(tile, (l * 12, 0))

    output_img.save(img)
    logger.info("已还原图片!")


def get_x():
    bg_img = cv2.imread("captcha_bg.jpg", 0)  # 背景图片（灰度模式）
    slider_img = cv2.imread("captcha_slice.jpg", 0)  # 滑块图片（灰度模式）
    # 边缘检测
    bg_edge = cv2.Canny(bg_img, 100, 200)
    slider_edge = cv2.Canny(slider_img, 100, 200)
    # 模板匹配
    result = cv2.matchTemplate(bg_edge, slider_edge, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    # 返回缺口的横坐标
    x = max_loc[0]
    logger.info(f"获取到缺块横坐标为: {x}")
    return x

    # slide = ddddocr.DdddOcr(det=False, ocr=False)
    # with open('captcha_fullbg.jpg', 'rb') as f:
    #     target_bytes = f.read()
    # with open('captcha_bg.jpg', 'rb') as f:
    #     background_bytes = f.read()
    # res = slide.slide_comparison(target_bytes, background_bytes)
    # print("x:", res.get('target')[0])
    # return res.get('target')[0]

def __ease_out_expo(sep):
    """
    缓动函数 easeOutExpo
    参考：https://easings.net/zh-cn#easeOutExpo
    """
    if sep == 1:
        return 1
    else:
        return 1 - pow(2, -10 * sep)

def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(-50, -10), random.randint(-50, -10), 0],
        [0, 0, 0],
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    t = random.randint(50, 100)
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t += random.randint(10, 20)
        if x == _x:
            continue
        slide_track.append([x, _y, t])
        _x = x
    slide_track.append(slide_track[-1])
    pass_time = slide_track[-1][-1]
    return slide_track, pass_time

def get_array(s):
    c = []
    for d in range(len(s)):
        if d == 32:
            break
        u = ord(s[d])
        while a(c, u % 32):
            u += 1
        c.append(u % 32)
    return c

def a(n, t):
    if t in n:
        return True
    return False

def encrypt(n):
    if not n:
        return ""
    t = ""
    i = "V587"
    e = 50133
    for r in range(len(n)):
        o = ord(n[r])
        o ^= ord(i[e % len(i)])
        e = (e + 1) % len(i)
        t += chr(o)
    return t





if __name__ == '__main__':
    sid, p1, p2, aid = request2()
    download_captcha(p1, p2)
    array = get_array(p1.split('/')[4].split('.')[0])
    parse_captcha(array, "captcha_bg.jpg")
    x = get_x()
