# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: hotboard_demo.py
@time: 2024/7/3 17:49
"""


import requests
import execjs

cookies = {
    'msToken': 'H6r2TPqaAR-7KyWHmKvx1z6n07hIlIL3PHJlr9ORGKSUUX6WE64OOdg7_yWtbn3er2Q-Ju5Bml27H1VMDhOrPS3ZE09zjAsaD2jnDeu2',
    '__ac_signature': '_02B4Z6wo00f01IqxwJAAAIDBpDYNul6LOkyKkcQAAETYde',
    'tt_webid': '7387297395741525542',
    'gfkadpd': '24,6457',
    'ttcid': '4c15ab780bc7415bb6f49d149afa550844',
    'x-web-secsdk-uid': 'd2da990f-6cdc-452b-9b71-16a9a1cba552',
    'local_city_cache': '%E5%8C%97%E4%BA%AC',
    's_v_web_id': 'verify_ly5h6kbl_dolYQtuZ_Uy1c_42bD_8bkl_UU8pLrapvj19',
    'csrftoken': '34d962e4e950fdffe1c071c682bb169f',
    '_ga': 'GA1.1.773850983.1719989238',
    '_ga_QEHZPBE5HH': 'GS1.1.1719995770.2.1.1719996739.0.0.0',
    'tt_scid': 'IXEB5qrGsND6B.1jvAEvDfqLcVTmSOLJszaKfOx5DRsRHlpeAqnb1oY.w--c7BUt2b2f',
    'ttwid': '1%7CVtTii9AJjKYniE8K6TqqyYjEQYROz9Wq4_PdjLMDRAI%7C1719996742%7C8b5b25c19562532e28ca501cdc350ff17f792d3703fd8e6e2584ffbd256d0ebb',
}

cookie = 'msToken=H6r2TPqaAR-7KyWHmKvx1z6n07hIlIL3PHJlr9ORGKSUUX6WE64OOdg7_yWtbn3er2Q-Ju5Bml27H1VMDhOrPS3ZE09zjAsaD2jnDeu2; __ac_signature=_02B4Z6wo00f01IqxwJAAAIDBpDYNul6LOkyKkcQAAETYde; tt_webid=7387297395741525542; gfkadpd=24,6457; ttcid=4c15ab780bc7415bb6f49d149afa550844; x-web-secsdk-uid=d2da990f-6cdc-452b-9b71-16a9a1cba552; local_city_cache=%E5%8C%97%E4%BA%AC; s_v_web_id=verify_ly5h6kbl_dolYQtuZ_Uy1c_42bD_8bkl_UU8pLrapvj19; csrftoken=34d962e4e950fdffe1c071c682bb169f; _ga=GA1.1.773850983.1719989238; _ga_QEHZPBE5HH=GS1.1.1719995770.2.1.1719996739.0.0.0; tt_scid=IXEB5qrGsND6B.1jvAEvDfqLcVTmSOLJszaKfOx5DRsRHlpeAqnb1oY.w--c7BUt2b2f; ttwid=1%7CVtTii9AJjKYniE8K6TqqyYjEQYROz9Wq4_PdjLMDRAI%7C1719996742%7C8b5b25c19562532e28ca501cdc350ff17f792d3703fd8e6e2584ffbd256d0ebb'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    'cookie': cookie,
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.toutiao.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

api_url = "https://www.toutiao.com/hot-event/hot-board/"

# 读取本地 JavaScript 文件内容
with open('./hotboard_test.js', 'r', encoding='utf-8') as file:
    js_code = file.read()
ctx = execjs.compile(js_code)

# 调用 executeCode 函数
post_url = {
    "url": f"{api_url}?origin=toutiao_pc"
}
_signature = ctx.call("get_signature", post_url, cookie)
print(_signature)

params = {
    'origin': 'toutiao_pc',
    '_signature': _signature,
}

response = requests.get(url=api_url, params=params, headers=headers)
print(response.json())

