# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: verify_demo.py
@time: 2024/7/6 14:50
"""

# 适用版本 jsv 5.1.49   version 0.1.75
import copy
import pprint
import re
from io import BytesIO

import execjs
import requests
from PIL import Image

from 公用方法.图片解混淆 import reduction_image
from 公用方法.滑动轨迹 import generate_track
from 公用方法.计算缺口距离 import calculate_distance_model_1

pp = pprint.PrettyPrinter(indent=4)

requests.packages.urllib3.disable_warnings()

temp_c = "668e31b6YQlzacN1TtsOj2r2PuR734xTiTXb2f71"
ak = "99de95ad1f23597c23b3558d932ded3c"
aid = "dx-1720767910997-41349549-3"
cid = "12769118"
_r = "0.9683849386451"


class DX_Slider(object):
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.dingxiang-inc.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.dingxiang-inc.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.constid = temp_c
        self.bg_w = 380
        self.bg_h = 165
        self.base_param = {
            "w": self.bg_w,
            "h": self.bg_h,
            "jsv": "5.1.49",
            "uid": "",
        }
        self.a_base_param = {
            "s": 50,
            "wp": 1,
            "de": 0,
            "lf": 0,
            "tpc": ""
        }
        self.a_base_param.update(self.base_param)

        self.ak = ak
        self.aid = aid
        self.cid = cid
        self._r = _r
        self.sid = ""
        self.session = requests.session()

    def get_captcha_images(self, c=None):
        # 获取滑块图片数据
        if not c:
            params = copy.deepcopy(self.a_base_param)
            params.update({
                "ak": self.ak,
                "c": "",
                "aid": self.aid,
                "cid": self.cid,
                "_r": self._r
            })
        else:
            if not self.sid:
                # TODO 获取 sid
                pass

            params = copy.deepcopy(self.a_base_param)
            params.update({
                "ak": self.ak,
                "c": c,
                "aid": self.aid,
                "cid": self.cid,
                "_r": self._r,
                "code": "undefined",
                "m": "",
                "sid": self.sid,
                "wtf": "false"
            })

        a_api_res = self.session.get("https://cap.dingxiang-inc.com/api/a", headers=self.headers, params=params,
                                     verify=False).json()

        # 处理图片
        img_url_base = "https://static4.dingxiang-inc.com/picture"
        image_item = {
            "sid": a_api_res["sid"],
            "cid": a_api_res["cid"],
            "y": a_api_res["y"],  # 用于控制页面上滑块上的显示位置
            "bg_url": img_url_base + a_api_res["p1"],  # 等待还原背景图
            "slider_url": img_url_base + a_api_res["p2"],  # 滑块底图
        }
        return image_item

    @staticmethod
    def handle_bg_image(bg_url):
        img_response = requests.get(bg_url)

        img_data = BytesIO(img_response.content)
        old_img = Image.open(img_data)
        old_img.save("old_bg.png")

        old_image_hash = re.search(r"https://.*?\.dingxiang-inc.com/picture/dx/.*?/.*?/(.*?).webp", bg_url).group(1)
        print("old_bg_image_hash：", old_image_hash)

        with open("image_array.js", encoding="utf-8") as f:
            image_array_jscode = f.read()

        old_image_array = execjs.compile(image_array_jscode).call("get_array", old_image_hash)
        print("old_bg_image_array：", old_image_array)

        reduction_image(old_image_array, old_img)

    @staticmethod
    def handle_slide_image(slide_url):
        img_response = requests.get(slide_url)

        img_data = BytesIO(img_response.content)
        slide_img = Image.open(img_data)
        slide_img.save("slider.png")

    # 格式化图片
    def image_processing(self):
        # bg.png
        # resize图片大小， 入口参数为一个tuple， 新的图片的大小
        image_path_1 = Image.open("new_bg.png")
        image_size_1 = image_path_1.resize((self.bg_w, self.bg_h))
        # 处理图片后存储路径及存储格式
        image_size_1.save("new_bg.png")

        # slider.png
        # resize图片大小， 入口参数为一个tuple， 新的图片的大小
        image_path_2 = Image.open("slider.png")
        image_size_2 = image_path_2.resize((64, 55))
        # 处理图片后存储路径及存储格式
        image_size_2.save("slider.png")

    # 滑块缺口验证
    def verify(self, constid, image_item, distance):
        v1_url = "https://cap.dingxiang-inc.com/api/v1"
        with open("verify_generate_params.js", encoding="utf-8") as f:
            ac_jscode = f.read()

        track = generate_track(distance)
        print("滑动轨迹：", track)
        ac = execjs.compile(ac_jscode).call("get_ac", image_item["sid"], track, distance, image_item["y"])
        post_data = copy.deepcopy(self.base_param)
        post_data.update({
            "ac": ac,
            "ak": self.ak,
            "c": constid,
            "aid": self.aid,
            "sid": image_item["sid"],
            "x": str(distance),
            "y": str(image_item["y"]),
        })
        pp.pprint(post_data)

        response = self.session.post(v1_url, headers=self.headers, data=post_data, verify=False)
        print(response.text)

    def test_verify(self):
        v1_url = "https://cap.dingxiang-inc.com/api/v1"
        post_data = {
            "jsv": "5.1.49",
            "uid": "",
            "x": "234",
            "y": "65",
            "w": "380",
            "h": "165",
            "ak": "99de95ad1f23597c23b3558d932ded3c",
            "c": "668e31b6YQlzacN1TtsOj2r2PuR734xTiTXb2f71",
            "sid": "6cea32df145868bab0c4b4ec3134cfac",
            "aid": "dx-1720775842185-51344003-4",
            "ac": "4358#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"
        }
        pp.pprint(post_data)

        response = self.session.post(v1_url, headers=self.headers, data=post_data, verify=False)
        print(response.text)

    # 处理流程
    def run(self):
        # 处理接口参数 c
        # constid = self.handle_const_id()
        constid = self.constid

        # 验证码图片数据
        image_item = self.get_captcha_images(constid)

        # 处理背景图
        self.handle_bg_image(image_item["bg_url"])

        # 处理滑块图
        self.handle_slide_image(image_item["slider_url"])

        # 调整图片大小
        self.image_processing()

        # 计算缺口距离
        distance = calculate_distance_model_1("new_bg.png", "slider.png")

        # 滑块验证
        self.verify(constid, image_item, distance)


if __name__ == "__main__":
    DX_Slider().run()
