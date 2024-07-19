# encoding: utf-8
"""
@author: The King
@project: js_project
@file: SearchList.py
@time: 2024/7/18 18:08
"""


import requests

cookies = {
    'GW1gelwM5YZuS': '60bR3naMVFe2HQ7iUbWTFXeTPOZlSmbPDbU7sS5ef6q6Tf1imydQUjRZk03XESA2KsbSeAIFbOmBOzSqrCj4aG7q',
    'ae51635ca5836b4864': '94ee5fb45ad7f8f15d2d00578ab61262',
    'ASP.NET_SessionId': 'dfkn1anm5tyqaaw0ljhoxclh',
    'LIBUSERIDCOOKIE': '0',
    'LIBUSERNAMECOOKIE': '',
    'f6324025fe': '4237cb9854aa9bb989454994e23dd86c',
    'Hm_lvt_17262dc62ce874a510e9c97140f381d6': '1721215940,1721288592,1721288678',
    'HMACCOUNT': '75004FF0BC571D74',
    'Hm_lvt_fee827c3dc795c5122daf5ee854c1683': '1721215940,1721288592,1721288678',
    '__root_domain_v': '.cqvip.com',
    '_qddaz': 'QD.723421288677870',
    '_qddab': '3-scv39j.lyqyu4c2',
    'user_behavior_flag': '5f2f1bdd-fdef-4fb4-a276-4f6bbcd15e67',
    'Hm_lpvt_17262dc62ce874a510e9c97140f381d6': '1721289385',
    'Hm_lpvt_fee827c3dc795c5122daf5ee854c1683': '1721289385',
    'LIBUSERCOOKIE': 'Oosn4ui%2b3LJX5JgKzYZ95idPxkVpETqyjRyS8c7iRf0HCVRXosYw7LzYtXoz%2fa2BcXU26V2QLFlxOL0kv7VPUkvzdYaV9EU4zMzj800rsYtQuX9ryhpLIizuSAIe3hk6GwzBwj9ndxfj9gouCCC41nJPa3kz4Aq60ZbfvzhIbdNDO05tHXtM%2bqJFze2iFrDStikRXvCNFPv%2bQzW2WUN9xOfIAQPLKSL4YS3KmKDV3T%2fFz6UwEeqyrbEHVxKK9WHvvcd19xVQ6BAhAJLQacRqoxSzoR7EMSYR3626VyNUBTsfk6tirRwSImyejyTnyUjf3%2f3Rwo6wXmEJc4dz7fiyptFiT6rPpUt%2fUf%2bjY0BTiQX67ctk3avZ9V8wgSBWxCT%2b%2f3h4YGOXlX8zSnMQ6gWL1rUl2QlzJkoiBE2BW1Mzw30%3d',
    'search_isEnable': '1',
    'GW1gelwM5YZuT': '0TvJxrgUsshilPA5zItft5SW5jcUeXt_DzD3qQ9tX98Vv86xQYC0JRNFDxgnXTTnoNo1_DEougGfg7ujIu6XqxW4sjw53LU3EAa0GPaiPt2CxX8hUWxCvpNYYighp33HBgTGWnSMxrHWcAUJaWZ5EIDgInuzzClaLUukJaLtrofU_AeWwVdJd8hRg.v2GFdy4481t3BEBEpsPd94yUOjw2Pwm2WEJMQCwvxW6f.uuWaxATIFi0VKQHPaxGiZe6oSY6.MOMXUNzW_61aiJ7hyjltu9WHEN378gIwQ0vd8rGBPCqr2w_23BOSKKEJj_oI3R72Av64eiAhRles7jzT7.VmYq61FFWw2USmztPSvUqRbKDD1RXGlmdEVvLrPcbNVeaKG5rjshkAxhLDR83JS9XyAkw.N9vQD7Lkd4oY8q1IHoZUGW_68oDx4x2QY3_2cQ',
}


headers = {
    'accept': 'text/html, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://lib.cqvip.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://lib.cqvip.com/Qikan/Journal/JournalGuid?from=index',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'X2sCXRB4': '0qP0TmGlqEtsQqVAKHoM74m3V7.wdCPDnIUv5G6BNH5LSvpUQxAozEtk74AjARhj0.mVCYynltz5KCJNYjx1cLPFZzKjUuXzv',
}

data = {
    'searchParamModel': '{"ObjectType":7,"SearchKeyList":[],"SearchExpression":null,"BeginYear":null,"EndYear":null,"UpdateTimeType":null,"JournalRange":null,"DomainRange":null,"ClusterFilter":"ZY=320#产业经济","ClusterLimit":0,"ClusterUseType":"Article","UrlParam":"","Sort":"1","SortField":null,"UserID":"0","PageNum":1,"PageSize":20,"SType":null,"StrIds":null,"IsRefOrBy":0,"ShowRules":"","IsNoteHistory":0,"AdvShowTitle":null,"ObjectId":null,"ObjectSearchType":0,"ChineseEnglishExtend":0,"SynonymExtend":0,"ShowTotalCount":0,"AdvTabGuid":""}',
}

response = requests.post('https://lib.cqvip.com/Search/SearchList', params=params, cookies=cookies, headers=headers, data=data)
