"""
url : https://captcha1.scrape.center/
登陆 + 滑动验证码（极验3代）
主要参数 w (滑动轨迹值)
time： 2025年7月12日
"""

import io
import json
import math

import cv2
import requests
import time
import execjs
from PIL import Image
import random
import ddddocr
import subprocess

from loguru import logger

pic_base_url = 'https://static.geetest.com/'
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://captcha1.scrape.center/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Storage-Access": "active",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}


def get_gt_challenge(t):
    """
    第一步
    通过13位时间戳来获取gt值，gt值后续不会改变。
    """
    url = f'https://captcha1.scrape.center/api/init?t={t}'
    response = requests.get(url)
    data = json.loads(response.text)
    gt = data['gt']
    challenge1 = data['challenge']
    print("-------------------------------------------------------------")
    print("First : 获取gt和challenge值。")
    print("gt :", gt)
    print("challenge1 :", challenge1)
    print("-------------------------------------------------------------")
    return gt, challenge1


def gettype(gt):
    """
    第二步
    将获取的gt值传入新的请求，网站上获取到验证码服务商的JS文件，进行后续的加密操作。
    """
    url = f"https://api.geetest.com/gettype.php?gt={gt}&callback=geetest_{math.floor(time.time() * 1000)}"
    response = requests.get(url)
    print("Second gettype:",response.text)
    print("-------------------------------------------------------------")


def get_php_1(gt, challenge):
    """
    第三步
    将生成的challenge值和获取的gt值传入https://api.geetest.com/get.php?中，返回结果中有c值（一个固定的数组）和 s值 （每次请求都会变），c参与后续加密运算。
    """
    url = "https://api.geetest.com/get.php"
    params = {
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn", # 定值
        "pt": "0", # 定值
        "client_type": "web", # 定值
        "w": "", # 触发无感验证的参数，这里传空值也可以。
        "callback": f"geetest_{math.floor(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text.split("(")[1].replace(")", ""))
    c = data.get("data").get("c")
    s = data.get("data").get("s")
    print("Third gettype:","c :", c, "s :", s)
    print("-------------------------------------------------------------")
    return c, s

def ajax(gt, challenge):
    """
    第四步
    获取验证码的形式（滑动或点选等其他类型）
    """
    url = "https://api.geevisit.com/ajax.php"
    params = {
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",  # 定值
        "pt": "0",  # 定值
        "client_type": "web",  # 定值
        "w": "",  # 触发无感验证的参数，这里传空值也可以。
        "callback": f"geetest_{math.floor(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text.split("(")[1].replace(")", ""))
    type = data.get("data").get("result")
    print("Fourth ajax: 获取到的验证码类型为", type)
    print("-------------------------------------------------------------")


def get_php_2(gt, challenge):
    """
    第五步
    获取背景图以及新的s值，这里的s值参与加密运算，在原有的challenge值末尾加盐。将加盐后的challenge值传入验证请求的params中。
    """
    url = "https://api.geevisit.com/get.php"
    params = {
        "is_next": "true",
        "type": "slide3",
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        "https": "true",
        "protocol": "https://",
        "offline": "false",
        "product": "embed",
        "api_server": "api.geevisit.com",
        "isPC": "true",
        "autoReset": "true",
        "width": "100%",
        "callback": f"geetest_{math.floor(time.time() * 1000)}"
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text.split("(")[1].replace(")", ""))
    fullbg = data.get("fullbg")
    bg = data.get("bg")
    slice = data.get("slice")
    s = data.get("s")
    id = data.get("id")
    challenge2 = data.get("challenge")
    print("Fifth php2:")
    print("fullbg:", fullbg, "bg:", bg, "slice:", slice)
    print("s:", s, "id:", id, "challenge2:", challenge2)
    print("-------------------------------------------------------------")
    return fullbg, bg, slice, s, id, challenge2


def download_captcha(fullbg, bg, slice):
    """
    下载传回的图片，为后续计算滑动距离轨迹做铺垫。
    """

    response = requests.get(pic_base_url+fullbg, headers=headers)
    with open("captcha_fullbg.jpg", "wb") as f:
        f.write(response.content)

    response = requests.get(pic_base_url+bg, headers=headers)
    with open("captcha_bg.jpg", "wb") as f:
        f.write(response.content)

    response = requests.get(pic_base_url+slice, headers=headers)
    with open("captcha_slice.jpg", "wb") as f:
        f.write(response.content)


def parse_bg_captcha(img):
    """
    清洗图片背景图还原
    :param img: 图片路径str/图片路径Path对象/图片二进制
    eg: 'assets/bg.webp'
        Path('assets/bg.webp')
    :param save_path: 保存路径, <type 'str'>/<type 'Path'>; default: None
    :return: 还原后背景图 RGB图片格式
    """
    if isinstance(img, str):
        _img = Image.open(img)
    elif isinstance(img, bytes):
        _img = Image.open(io.BytesIO(img))


    # 图片处理顺序，左值
    _Ge = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43,
           42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    w_sep, h_sep = 10, 80

    # 还原后的背景图
    new_img = Image.new('RGB', (260, 160))

    for idx in range(len(_Ge)):
        x = _Ge[idx] % 26 * 12 + 1
        y = h_sep if _Ge[idx] > 25 else 0
        # 从背景图中裁剪出对应位置的小块
        img_cut = _img.crop((x, y, x + w_sep, y + h_sep))
        # 将小块拼接在新图中
        new_x = idx % 26 * 10
        new_y = h_sep if idx > 25 else 0
        new_img.paste(img_cut, (new_x, new_y))

    new_img.save(img)
    return new_img

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


def get_geetest_validate(gt, challenge, w):
    """
    第六步
    加密轨迹值，传入w参数，获得验证成功的参数。
    """
    url = "https://api.geevisit.com/ajax.php"
    params = {
        "gt": gt,
        "challenge": challenge,
        "lang": "zh-cn",
        "%24_BCm": "0",
        "client_type": "web",
        "w": w
    }
    response = requests.get(url, headers=headers, params=params)
    data = json.loads(response.text.split("(")[1].replace(")", ""))
    validate = data.get("validate")
    print("Finally geetest_validate:", response.text)
    print("-------------------------------------------------------------")
    return validate


def login(challenge, validate):
    """
    最后将通过的validate传入登陆验证接口中，
    """
    url = "https://captcha1.scrape.center/api/login"
    data = {
        "username": "admin",
        "password": "admin",
        "captcha": {
            "geetest_challenge": challenge,
            "geetest_validate": validate,
            "geetest_seccode": f"{validate}|jordan",
            "status": 1,
            "type": "geetest"
        }
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data)
    print(response.text)



def get_w(track_array, t, s, challenge, passtime):
    """
    传入参数到JS文件中，进行加密运算得到w的值。
    """
    # 构造参数对象
    args = {
        "track_array": track_array,
        "t": t,
        "s": s,
        "challenge": challenge,
        "passtime": passtime,
    }
    print("传入的参数为：",args)
    # 调用 Node.js 执行脚本
    cmd = ["node", "captcha1.js", json.dumps(args)]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        raise Exception(f"Error calling get_W: {stderr}")
    w = stdout.strip()
    print(f"w: {w}")
    return w

def main():
    timestamp = math.floor(time.time() * 1000) # 构造时间戳
    gt, challenge1 = get_gt_challenge(timestamp) # 发送请求获取gt和challenge
    gettype(gt) # 获取验证码服务商文件版本
    c, s1 = get_php_1(gt, challenge1) # 获取c值
    ajax(gt, challenge1) # 获取验证码类型
    fullbg, bg, slice, s2, id, challenge2 = get_php_2(gt, challenge1) # 获取图片地址，以及新的s值，s值进行加密运算，challenge值进行加盐传入验证的请求
    download_captcha(fullbg, bg, slice) # 下载图片，图片初始为被打乱的状态
    parse_bg_captcha('captcha_bg.jpg') # 还原被打乱的图片
    parse_bg_captcha('captcha_fullbg.jpg') # 还原被打乱的图片
    x = get_x() # 对比缺口，获取滑动的距离
    slide_track, passtime = get_slide_track(x) # 模拟滑动轨迹
    w = get_w(slide_track, x, s2, challenge2, passtime)
    validate = get_geetest_validate(gt, challenge2, w) # 获取加密后的w值，然后发送请求
    login(challenge2, validate)


if __name__ == '__main__':
    main()