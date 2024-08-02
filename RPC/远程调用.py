# encoding: utf-8
"""
@author: The King
@project: JSProjects
@file: 远程调用.py
@time: 2024/7/29 14:35
"""

import json
import requests


url = "http://127.0.0.1:12080/go"
data = {
    "group": "location",
    "name": "mycode",
    "action": "getData",
    "param": json.dumps({"param_1_name": "xxx", "param_2_name": "xxx"})
}

res = requests.post(url, data=data)
print(res.text)
