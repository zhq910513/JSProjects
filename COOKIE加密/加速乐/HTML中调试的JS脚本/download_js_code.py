# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: download_js_code.py
@time: 2024/7/3 11:14
"""
import re

import execjs
import requests


url = "https://www.mps.gov.cn/index.html"
headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": url,
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

first_response = requests.get(url=url, headers=headers)
first_response.encoding = "utf-8"
jsl_cookie = requests.utils.dict_from_cookiejar(first_response.cookies)   # 服务器返回的cookie 是jarcookie对象
__jsl_clearance_s_jscode = re.findall("cookie=(.*?);location", first_response.text, re.S)[0]
jsl_cookie["__jsl_clearance_s"] = execjs.eval(__jsl_clearance_s_jscode).split(";")[0].split("=")[1]
print(jsl_cookie)


second_response = requests.get(url=url, headers=headers, cookies=jsl_cookie)
second_response.encoding = "utf-8"
print(second_response.text)
with open("js_code.html", "w", encoding="utf-8") as f:
    f.write(second_response.text)
