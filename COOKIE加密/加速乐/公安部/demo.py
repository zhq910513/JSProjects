# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: homefeed_demo.py
@time: 2024/7/1 14:50
"""
import hashlib
import json
import re

import execjs
import requests


class Set_Jsl_Cookie(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": self.url,
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.session = requests.session()
        self.set_first_cookie()
        self.set_second_cookie()

    def set_first_cookie(self):
        first_response = self.session.get(url=self.url, headers=self.headers)
        try:
            first_content = re.findall("cookie=(.*?);location", first_response.text, re.S)[0]
            jsl_clearance_s = str(execjs.eval(first_content)).split(";")[0].split("=")
            self.session.cookies[jsl_clearance_s[0]] = jsl_clearance_s[1]
        except IndexError:
            print("Error: Unable to extract cookie from the first response.")
            return

    def set_second_cookie(self):
        self.headers["Referer"] = self.url

        def set_jsl_clearance_s(data):
            def get_hash(string, model):
                model = model.lower()
                if model == "sha1":
                    return hashlib.sha1(string.encode("utf-8")).hexdigest()
                elif model == "sha256":
                    return hashlib.sha256(string.encode("utf-8")).hexdigest()
                else:
                    return hashlib.md5(string.encode("utf-8")).hexdigest()

            for e in range(len(data["chars"])):
                for r in range(len(data["chars"])):
                    text = data["bts"][0] + data["chars"][e:e + 1] + data["chars"][r:r + 1] + data["bts"][1]
                    if get_hash(text, data["ha"]) == data["ct"]:
                        return text

        second_response = self.session.get(url=self.url, headers=self.headers)
        try:
            second_content = json.loads("{" + re.findall("go\({(.*?)}\)", second_response.text, re.S)[0] + "}")
            self.session.cookies[second_content["tn"]] = set_jsl_clearance_s(second_content)
        except IndexError:
            print("Error: Unable to extract data from the second response.")
            return

    def test(self):
        test_response = self.session.get(url=self.url, headers=self.headers)
        test_response.encoding = "utf-8"
        print(test_response.text)


if __name__ == '__main__':
    test_url = "https://www.mps.gov.cn/index.html"

    # 不处理加速乐的结果
    # cookie = "__jsluid_s=c788470a6f4047213b68aaabbb4df5e4; __jsl_clearance_s=1719819894.283|0|iz1f93iSEGJF3YKiNiTiIq%2FsJyU%3D"
    # test_headers_no_jsl = {
    #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    #         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7",
    #         "Cache-Control": "no-cache",
    #         "Connection": "keep-alive",
    #         "Pragma": "no-cache",
    #         "Referer": test_url,
    #         "Cookie": cookie,
    #         "Sec-Fetch-Dest": "document",
    #         "Sec-Fetch-Mode": "navigate",
    #         "Sec-Fetch-Site": "same-origin",
    #         "Upgrade-Insecure-Requests": "1",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    #         "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    #         "sec-ch-ua-mobile": "?0",
    #         "sec-ch-ua-platform": "\"Windows\""
    #     }
    # test_response_no_jsl = requests.get(url=test_url, headers=test_headers_no_jsl)
    # test_response_no_jsl.encoding = "utf-8"
    # print(test_response_no_jsl.text)

    # 处理加速乐的结果
    Set_Jsl_Cookie(test_url).test()
