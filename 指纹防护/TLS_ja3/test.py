# encoding: utf-8
"""
@author: The King
@project: JSProjects
@file: 测试数组变化.py
@time: 2024/7/20 22:59
"""
import pprint
import requests

pp = pprint.PrettyPrinter(indent=4)


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://tls.browserleaks.com/json', headers=headers)
pp.pprint(response.json())

# 绕过
# 方法一  修改底层代码impersonate
from curl_cffi import requests as creq

c_resp = creq.get('https://tls.browserleaks.com/json', headers=headers, impersonate="chrome101")
pp.pprint(c_resp.json())


# 方法二
