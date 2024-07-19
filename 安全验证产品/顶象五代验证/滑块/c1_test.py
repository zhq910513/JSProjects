import execjs
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
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

with open("verify_generate_params.js", encoding="utf-8") as f:
    ac_jscode = f.read()

ac = execjs.compile(ac_jscode).call("get_ac", "", [], 0, 0)
print(ac)

data = {
    '_t': '46268',
    'Param': ac
    # 'Param': '4282#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',
}

response = requests.post('https://constid.dingxiang-inc.com/udid/c1', headers=headers, data=data)
print(response.json())
