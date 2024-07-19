# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: verify_demo.py
@time: 2024/7/8 20:40
"""
# 适用 SDK版本 1.1.3/rversion版本 1.0.4

import json
import pprint
import re
from io import BytesIO

import execjs
import requests
from PIL import Image

from 公用方法.滑动轨迹 import generate_track
from 公用方法.计算缺口距离 import calculate_distance_model_2

pp = pprint.PrettyPrinter(indent=4)


class ShuMeiSlider:
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Origin': 'https://www.ishumei.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.ishumei.com/trial/captcha.html',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.session = requests.session()
        self.organization = "d6tpAY1oV0Kv5jRSgxQr"
        self.sdkver = "1.1.3"
        self.model = "slide"
        self.rversion = "1.0.4"
        self.callback = "callback"
        self.bg_height = 150
        self.bg_width = 300

    @staticmethod
    def get_captcha_uuid():
        with open("register_captcha_uuid_source.js", encoding="utf-8") as f:
            ac_jscode = f.read()

        return execjs.compile(ac_jscode).call("getCaptchaUuid")

    @staticmethod
    def get_encrypt_content(_data):
        with open("verify_source.js", encoding="utf-8") as f:
            jscode = f.read()

        return execjs.compile(jscode).call("handle_encrypt", _data)

    def get_register_data(self, captcha_uuid):
        register_params = {
            'data': '{}',
            'sdkver': self.sdkver,
            'model': self.model,
            'rversion': self.rversion,
            'organization': self.organization,
            'appId': 'default',
            'channel': 'DEFAULT',
            'callback': self.callback,
            'captchaUuid': captcha_uuid,
            'lang': 'zh-cn',
        }

        response = requests.get('https://captcha1.fengkongcloud.cn/ca/v1/register', params=register_params,
                                headers=self.headers)
        if response.status_code == 200:
            data = re.findall("callback\((.*?)\)", response.text, re.S)
            if data:
                data_json = json.loads(data[0])
                # data_json = temp_data

                # 处理图片
                img_url_base = "https://castatic.fengkongcloud.cn"
                image_item = {
                    "rid": data_json["detail"]["rid"],
                    "k": data_json["detail"]["k"],
                    "l": data_json["detail"]["l"],
                    "bg_url": img_url_base + data_json["detail"]["bg"],  # 等待还原背景图
                    "slider_url": img_url_base + data_json["detail"]["fg"],  # 滑块底图
                }
                return image_item

    @staticmethod
    def handle_bg_image(bg_url):
        print(bg_url)
        img_response = requests.get(bg_url)

        img_data = BytesIO(img_response.content)
        old_img = Image.open(img_data)
        old_img.save("bg.png")

    @staticmethod
    def handle_slide_image(slide_url):
        print(slide_url)
        img_response = requests.get(slide_url)

        img_data = BytesIO(img_response.content)
        slide_img = Image.open(img_data)
        slide_img.save("slider.png")

    # 格式化图片
    def image_processing(self):
        # bg.png
        # resize图片大小， 入口参数为一个tuple， 新的图片的大小
        image_path_1 = Image.open("bg.png")
        image_size_1 = image_path_1.resize((self.bg_width, self.bg_height))
        # 处理图片后存储路径及存储格式
        image_size_1.save("bg.png")

        # slider.png
        # resize图片大小， 入口参数为一个tuple， 新的图片的大小
        image_path_2 = Image.open("slider.png")
        image_size_2 = image_path_2.resize((45, 150))
        # 处理图片后存储路径及存储格式
        image_size_2.save("slider.png")

    # 滑块缺口验证
    def verify(self, captcha_uuid, image_item, distance):
        track = generate_track(distance)
        print(track)

        _data = {
            "je": distance / 300,  # 滑动距离
            "mu": str(track).replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", ""),  # 滑动轨迹
            "ww": track[-1][-1],  # 滑动时间
            "nu": self.bg_width,
            "dy": self.bg_height
        }

        encrypt_data = self.get_encrypt_content(_data)
        pp.pprint(encrypt_data)

        verify_params = {
            'xy': 'YabT6nmJOC0=',
            'rid': image_item["rid"],
            'protocol': '180',
            'tb': '3jSn4gNaAVM=',
            'callback': self.callback,
            'nu': encrypt_data["nu"],
            'ww': encrypt_data["ww"],
            'jo': 'l3aEINYnwpY=',
            'ostype': 'web',
            'mu': encrypt_data["mu"],
            'mp': 'WYfkIZp7GoA=',
            'organization': self.organization,
            'sdkver': self.sdkver,
            'je': encrypt_data["je"],
            'oc': 'h9oFKi8cHpg=',
            'kq': 'mtlOTdT5LOE=',
            'rversion': self.rversion,
            'dy': encrypt_data["dy"],
            'en': 'y+ugz9NIWys=',
            'captchaUuid': captcha_uuid,
            'act.os': 'web_pc',
        }

        response = requests.get('https://captcha1.fengkongcloud.cn/ca/v2/fverify', params=verify_params,
                                headers=self.headers)
        print(response.text)

    # 处理流程
    def run(self):
        # 处理接口参数 captcha_uuid
        captcha_uuid = self.get_captcha_uuid()
        # captcha_uuid = "20240710001122dJZCzMWYwY3kCcfYAK"

        # 验证码图片数据
        image_item = self.get_register_data(captcha_uuid)

        # 处理背景图
        self.handle_bg_image(image_item["bg_url"])

        # 处理滑块图
        self.handle_slide_image(image_item["slider_url"])

        # 调整图片大小
        self.image_processing()

        # 计算缺口距离
        distance = calculate_distance_model_2("bg.png", "slider.png")

        # 滑块验证
        self.verify(captcha_uuid, image_item, distance)


if __name__ == "__main__":
    ShuMeiSlider().run()
    # ShuMeiSlider().calculate_distance("bg.png", "slider.png")
