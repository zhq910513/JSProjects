# encoding: utf-8
"""
@author: The King
@project: 逆向项目
@file: demo.py
@time: 2024/7/12 21:33
"""

from lxml import etree
import execjs
import requests

requests.packages.urllib3.disable_warnings()

# cookie 长度
# 网站生成   236
# 本地生成   257


class Set_Cookie(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Referer': 'http://zxgk.court.gov.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        }
        self.cookies = {}
        self.session = requests.session()
        self.set_first_cookie()

    def handle_js_content(self, resp):
        html = etree.HTML(resp.text)
        meta_content = html.xpath('//meta[2]/@content')[0]

        ts_code_1 = html.xpath('//script[1]/text()')[0]
        with open("cookie_ts_source_part_1.js", "w", encoding="utf-8") as f:
            f.write(ts_code_1)

        ts_code_2_link = html.xpath('//script[2]/@src')[0]
        if ts_code_2_link:
            ts_code_2_link = "http://zxgk.court.gov.cn" + ts_code_2_link
        ts_code_2 = self.session.get(url=ts_code_2_link, headers=self.headers, verify=False).text
        with open("cookie_ts_source_part_2.js", "w", encoding="utf-8") as f:
            f.write(ts_code_2)

        with open('./excute_js_code.js', 'r', encoding='utf-8') as f:
            excute_js_text = f.read()
            excute_js_text = excute_js_text.replace('meta_content', meta_content)
            excute_js_text = excute_js_text.replace('"ts_code_1"', ts_code_1)
            excute_js_text = excute_js_text.replace('"ts_code_2"', ts_code_2)

            get_yaT = execjs.compile(excute_js_text).call("get_yaT")
            self.cookies['lqWVdQzgOVyaT'] = get_yaT
            self.session.cookies.update(self.cookies)
            print("生成 lqWVdQzgOVyaT 的值: ", get_yaT)
            print("生成 lqWVdQzgOVyaT 的长度: ", len(get_yaT))

    def set_first_cookie(self):
        first_response = self.session.get(url=self.url, headers=self.headers)
        with open("./first_response.html", "w", encoding="utf-8") as f:
            f.write(first_response.text)

        print("第一次访问状态码：", first_response.status_code)
        try:
            self.cookies['lqWVdQzgOVyaS'] = first_response.cookies['lqWVdQzgOVyaS']
            self.session.cookies.update(self.cookies)
            self.handle_js_content(first_response)
        except IndexError:
            print("Error: Unable to extract cookie from the first response.")
            return

    def test(self):
        test_response = self.session.get(url=self.url, headers=self.headers, verify=False)
        test_response.encoding = "utf-8"
        print("第二次访问状态码：", test_response.status_code)
        print(test_response.text)


if __name__ == '__main__':
    test_link = "http://zxgk.court.gov.cn"
    Set_Cookie(test_link).test()
