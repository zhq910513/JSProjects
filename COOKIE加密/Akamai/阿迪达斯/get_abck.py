# encoding: utf-8
"""
@author: The King
@project: JSProjects
@file: get_abck.py
@time: 2024/8/1 21:25
"""
import execjs
import requests
from lxml import etree


link = 'https://www.adidas.com.cn/plp/kids_originals_superstar?page=1'


def get_js_link():
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    resp = requests.get(url=link, headers=headers)
    html = etree.HTML(resp.text)

    # 查找所有的 <script> 标签
    script_tags = html.xpath('//script[@type="text/javascript"]')

    # 确保至少有一个 <script> 标签
    if script_tags:
        # 获取最后一个 <script> 标签
        last_script = script_tags[-1]

        # 提取 src 属性
        return "https://www.adidas.com.cn" + last_script.get('src')
    else:
        print("没有找到任何指定类型的script标签")


def get_frist_cookie(js_link):
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=2',
        'referer': 'https://www.adidas.com.cn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    resp = requests.get(url=js_link, headers=headers)
    print("首次访问：", resp.cookies["_abck"])

    # 将 cookies 转换为字符串形式
    cookie = '; '.join([f"{cookie.name}={cookie.value}" for cookie in resp.cookies]) + ";"

    with open('./excute_js_code.js', 'r', encoding='utf-8') as f:
        excute_js_text = f.read()
        excute_js_text = excute_js_text.replace('js_link', link)
        excute_js_text = excute_js_text.replace('first_cookie', cookie)

        return cookie, execjs.compile(excute_js_text).call("encrypt_array")


def get_usefull_abck(js_link, cookie, sensor_data):
    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'text/plain;charset=UTF-8',
        'cookie': cookie,
        'origin': 'https://www.adidas.com.cn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.adidas.com.cn/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    data = sensor_data
    resp = requests.post(url=js_link, headers=headers, data=data,)
    print("再次访问：", resp.cookies["_abck"])


def run():
    _js_link = get_js_link()
    _cookie, _sensor_data = get_frist_cookie(_js_link)
    get_usefull_abck(_js_link, _cookie, _sensor_data)


if __name__ == '__main__':
    run()
