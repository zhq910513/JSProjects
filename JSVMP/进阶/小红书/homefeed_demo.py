# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: homefeed_demo.py
@time: 2024/7/5 12:09
"""
import json

import execjs
import requests

cookies = {
    'gid.sign': 'SW3/KTXl57mONOl80odGgLrmJa0=',
    'abRequestId': '0b6dbe190547857cdafdb403cf2cae21',
    'customerClientId': '342169266341676',
    'customer-sso-sid': '65b2237ef600000000000006',
    'x-user-id-ark.xiaohongshu.com': '5e8830ca0000000001009557',
    'a1': '18edb3cedecsru1wqpkagnqm8to45yb8wt46a25if50000213178',
    'webId': '047f355453a1b18da1796624246d1d8e',
    'gid': 'yYdfDqSiJqEDyYdfDqSdf9J2dSMF7yEAUT0k43iIA6Y9lK2842vDY0888JyqyWY80yJyJqfJ',
    'xsecappid': 'xhs-pc-web',
    'acw_tc': '79930ef908fcdda4283452395a2f688cc28d0bf24b52d263cf96bde9701b1f33',
    'web_session': '030037a12827806a1f36bed7ff214a673a8c87',
    'websectiga': '3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2',
    'sec_poison_id': 'd237fa4e-6911-453a-bb65-a053199c8598',
    'webBuild': '4.24.2',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'gid.sign=SW3/KTXl57mONOl80odGgLrmJa0=; abRequestId=0b6dbe190547857cdafdb403cf2cae21; customerClientId=342169266341676; customer-sso-sid=65b2237ef600000000000006; x-user-id-ark.xiaohongshu.com=5e8830ca0000000001009557; a1=18edb3cedecsru1wqpkagnqm8to45yb8wt46a25if50000213178; webId=047f355453a1b18da1796624246d1d8e; gid=yYdfDqSiJqEDyYdfDqSdf9J2dSMF7yEAUT0k43iIA6Y9lK2842vDY0888JyqyWY80yJyJqfJ; xsecappid=xhs-pc-web; acw_tc=79930ef908fcdda4283452395a2f688cc28d0bf24b52d263cf96bde9701b1f33; web_session=030037a12827806a1f36bed7ff214a673a8c87; websectiga=3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2; sec_poison_id=d237fa4e-6911-453a-bb65-a053199c8598; webBuild=4.24.2',
    'origin': 'https://www.xiaohongshu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    # 'x-b3-traceid': '6c8f99cbc6e64a8c',
    # 'x-s': 'XYW_eyJzaWduU3ZuIjoiNTIiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6ImZjMTg5Y2JiMWUxNTAzMWFmOGE5YzljM2JmZDE3MWY0Y2VmNjQyYmQ3OGM4Nzc1ZWFlNjI5MTE5NGZmMTAwNDBmNmM0OGIwM2ExNmUzZDAwYzBiMjkyM2M1ZmRhMmQ1YWQwNTc1MDMwNTY2NTA0MjE4ODgxNDNkOWFkNGRkYmQ5ODg4MTQzZDlhZDRkZGJkOWI1NmNjM2EzN2M2YTdhYWRlOTM2NTBhZGMzMzlkZTY0MGQwNzFlMjA5ZjczODE2MWM0YTMwY2I2NzcxNWY2ZWQ2NTUyMDNmYzY0NDUxY2U5NmM1NzM4N2M2YzgyNDY3ZmNmMzE3N2RjY2UyMzdhNzczMmJlZTlkOTJkNDM0NDk3OWY4ZjhlZjY4ODY5MDczODMwOWJlYjcwNjhiMTZmZTI0NmExZjZjN2M3ZTU5N2E2NGVmMjRmOTU5ZmRjZTA2OTgxNWZiY2UzYWJkOGQ3NGVlNTM2NjI0N2JmNTFhYjllZGUwMjY0MDc2YmQzZjAzNiJ9',
    # 'x-s-common': '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',
    # 'x-t': '1720161725408',
}

url_path = '/api/sns/web/v1/homefeed'
post_data = {
    "cursor_score": "",
    "num": 39,
    "refresh_type": 1,
    "note_index": 35,
    "unread_begin_note_id": "",
    "unread_end_note_id": "",
    "unread_note_count": 0,
    "category": "homefeed.food_v3",
    "search_key": "",
    "need_num": 14,
    "image_formats": ["jpg", "webp", "avif"],
    "need_filter_image": False
}
data = '{"cursor_score":"","num":39,"refresh_type":1,"note_index":35,"unread_begin_note_id":"","unread_end_note_id":"","unread_note_count":0,"category":"homefeed.food_v3","search_key":"","need_num":14,"image_formats":["jpg","webp","avif"],"need_filter_image":false}'

with open("homefeed_test.js", encoding="utf-8") as f:
    jscode = f.read()

x_s = execjs.compile(jscode).call("get_x_s", url_path, post_data)
print(x_s)

headers["x-s"] = x_s
response = requests.post(f'https://edith.xiaohongshu.com{url_path}', cookies=cookies, headers=headers, data=data)
print(response.json())
