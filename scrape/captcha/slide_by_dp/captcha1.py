"""
url : https://captcha1.scrape.center/
登陆 + 滑动验证码（极验3代）
采用自动化模拟滑动的方式过滑块验证码。选择DrissionPage进行数据包的监听和自动化操作。
"""
import json
import io
import time

import requests
import cv2
import random
from GTrace import GTrace
from PIL import Image
from loguru import logger
from DrissionPage import Chromium, ChromiumOptions

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

    print("图片下载完毕")

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
    print("已还原图片")
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




co = ChromiumOptions()

# 初始化浏览器
browser = Chromium()
page = browser.latest_tab
# 访问登陆页面
page.get('https://captcha1.scrape.center/')
time.sleep(3)
# 开始监听指定数据包
page.listen.start('https://api.geevisit.com/get.php?is_next=')

# 定位输入框和登陆按钮并执行动作
username = page.ele('x:(//input)[1]').input('admin')
time.sleep(1)
password = page.ele('x:(//input)[2]').input('admin')
time.sleep(1)
login = page.ele('x://button').click()
time.sleep(1)

# 获取所需数据（图片）
for packet in page.listen.steps():
    data = json.loads(packet.response.body.split("(")[1].replace(")", ""))
    fullbg = data.get("fullbg")
    bg = data.get("bg")
    slice = data.get("slice")
    download_captcha(fullbg, bg, slice)
    parse_bg_captcha('captcha_bg.jpg')  # 还原被打乱的图片
    parse_bg_captcha('captcha_fullbg.jpg')  # 还原被打乱的图片

    x = get_x()  # 对比缺口，获取滑动的距离

    before_x = 0
    before_y = random.uniform(-10, 10)
    before_t = 0
    page.actions.hold('x://div[@class="geetest_slider_button"]')  # 将鼠标放置在滑块移动按钮上，左键不松
    guiji = GTrace().get_mouse_pos_path(x)[1]  # get_slide_track(drag_distance+rush_x)

    for _ in guiji:
        # print(_, _[2] / 1000 - before_t)
        page.actions.move(_[0] - before_x, _[1] - before_y, duration=_[2] / 1000 - before_t)
        before_x, before_y, before_t = _[0], _[1], _[2] / 1000

    page.actions.release('x://div[@class="geetest_slider_button"]')  # 释放左键点击
