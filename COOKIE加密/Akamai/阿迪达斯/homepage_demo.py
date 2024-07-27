# encoding: utf-8
"""
@author: The King
@project: JSProjects
@file: homepage_demo.py
@time: 2024/7/20 17:26
"""


import requests

cookies = {
    'bm_sv': '266C941E462FA648E82492C79D3C049B~YAAQ7tfOF6B+3+OQAQAACQ865RiZbQv59256trzZF0FPrKPB9y8orUHJZuEHxPFCCHGxFUa2S19SqsraKMVQyrAS9PcLE3diCkepf2SRGSPDzjl5TXxOohIv9LMR9mtf4fc+a0XpAAA4tCW1BKSAeWDhWhymuunE6cGzwy7kstTyC/PIwRJ2MVhCqvCug6jzrh18yfTRoZantOzjnMEz6/9+1L4+S9EDRTs9DXD4UvhgoJQYoPJQ1jj6OSkLhM8fvVunbg==~1',
    'ak_bmsc': 'BD972095EB2B73F80005ACB2816A2650~000000000000000000000000000000~YAAQ7tfOFyif3+OQAQAAqL865Rhy18QvC4FNkuN6sVXH+EwMtL8pnK6AqAs3PnBpKIfL4cHxrQ+qQc0rcVZlXxJP03cLOpeD8T7H2c3mrlTYPLwSHqW538xWbCLpq2JtOZoi1dr7n0EqAJPPd+2whd88VKrm2PYKdpdWdUkgcFt2e1doVbweb2tm66iiP0/HUKbjzC0uMnLGHHo0eulv+Ws6VxGpyUuEKN5QusSVZOH071zAjOQQORt3fCf9pmgJlHART9FAvOqbJuzXyHGYVaQoDckIfShWEqTCEwukrxIesCyvhYpo9PVZV2KrOQlKk9KiexdWqZtOLs/zvtdehtaNX3JQMIYdHJpXrm593zgGzwWMG4MchnavLRhW76R8sAtgTGY/lX5K778=',
    'bm_sz': '479F56D2856BAA12C16F98EF2D644DE7~YAAQ7tfOFyqf3+OQAQAAqL865RjQGgK/8NptgMJXiWd3+gEFbcwQrNgbsrw06Rc3tdSpWh8d/fGcZLekuVbO0yJeb0Nni/Duad77v4mfs2/iGGebIMAGDdKD3dnngNadjL/0ld+q1bb9/oaN8WhM4JQxqRmeuJcA9IKfK0mPbn3AQIwe+7SGIivSgQIkMpiIZTgyN4pFALMXUKfHylTpuvajpy5stPMzSFq+Z5ORh90ZQDkAeArHABLlN+d5Y1rLjixM4B3B001YXLAnezKWe7RKetdwjA0x98AERF8GxD6u+g4Cb4N1umGqWPru6J1kOPu8Lv+ANCqubfjK353lFzAYgEw+c+hfWsMClt+zeu075PxZzbk5rIlMDQFOr6iB70KomcyCRbcYogZLi3sdiX1DXUFBZ5RGjTWcLfWj8HmKiiWrK0m6/9Fw8gJwBv5HjA==~3228230~4272184',
    '_abck': '4A2A81DB3A826A89C7AA5A905DC822E4~-1~YAAQ7tfOF4Of3+OQAQAANsE65QxVNy6gF+E5LQDT8lKZYrwmEegbqEgU2KCzQ7iSstjYh9Q2hN/OVQAKRy+F2E18cz7MtB5er4M6zqY7I2MOPDikiAjtzkqnb2CcGVVlRQr7WepC7pna8sGGjz//F67alK/8y9R6RhL0FQVKPi+OgibXiLseCuu9e+qu9FDn59/pheJmKfCmpFY1GZ6st8WyCT1nIVJvT72GEyF3xHHgyJrLtUde41qftKcItl0GCvgz+zcTDLO7Fq7jkXRaMi8ZAuI0ElVC/Fa8wxhiJLWipf0oRQmQddBaRbY2rQk29pjLm4IyEmE1GVQfzSReu/hsR9Av1Nu7NPEGpKkCzl4fIeZWtnc5yP9r/WkkokFJU1YzU293VF69/A==~-1~-1~-1',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1',
    'referer': 'https://www.adidas.com.cn/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.adidas.com.cn/qMl8VjcrR5/C2lZNfDd/FD/Q33aLN0wOuVG1b/OH4vDE9pBQ/LDo/iAD8bU0A',
    # cookies=cookies,
    headers=headers,
)
print(response.text)
