# encoding: utf-8
"""
@author: The King
@project: JSProjects
@file: homepage_demo.py
@time: 2024/7/20 17:26
"""


import requests

cookies = {
    # 'bm_sz': '9CBE164C1A2C8E3CFC6AFD90A725B3EC~YAAQ72+bG6FmI8mQAQAAnM9xzxiOQa2FxeU0A8rUUL3pkw0EhTbRomvV6WrE0ETvGErhkTpxHXjuY+XqdhN0jqDqGwekvIk8v9TPBKS0QUPfIbSDIMECK0DVPo+TX8of3nt3BjV3Kn+Pp/3C+qZjGKi6XpYexzKy7pjJ5sz2Ketd26k3gTBFzupRjRinEwQnTDSe3IN1jajpfgFZPaem01Sa0VLakRIFp8ni0MtqFBmMqrbVh2yXSGNDpRKrDm71n6bN8bWK+GjtgoPSMinqPIc5CTSP8KwDi05or84Eqcqs7yQbkpecYH3l99rpGcVc/jHQgEhSPaelCql+pK5j2cJDt9xI1h1xuAhxr2yEOFY8oYZ2FtXEWQIybn9muBqjD/6/Dgr6MEdHKYo2ugd+8gTKUmkuV8MWpZpuudPsircTN151/w==~4601669~3355201',
    # 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22190cf71d06aab5-04d5a63df21805-26001f51-1382400-190cf71d06bbc8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwY2Y3MWQwNmFhYjUtMDRkNWE2M2RmMjE4MDUtMjYwMDFmNTEtMTM4MjQwMC0xOTBjZjcxZDA2YmJjOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D',
    '_abck': 'D37677AC859512A8EB74C93DA3AD3F23~0~YAAQ72+bG6xmI8mQAQAAP9Nxzwwo9pdx+eJLWKxFhIXqhrYpwO48pcx7cnSFA0CGN9muVve5NmbO7tGmabRAs39xvG2juk7PONFPK+0ycogVHmHp+3sTt9/5Y57dvpn8xFUwht+2WfzJk0OeFV7f+s5H25wDGbSrkbehlvWSNvgVK/d+Fhk30FeqkkPbsqjXoM4QSuDYo1Xl/wudcrvCDyxZ5ExKDVQLFjhN1sjMeoqW5ReRwBXyj5hClpn4yIJwDAq+b7oNo/nNyqbRGC5l2c5zaj48pxN7zIQ/AwAmHyonSveMCwNI9YolsNTEOPjMTPZUrHfw1iEHXVZ96y54xlW206lRcssmX1/ucXgl5IfrMfh89zTvj7zfHw7CyIrujbvS5rZRAibsNcpM36Zcf8iE9QIlvUfT6X3oLRM6+DupAsYNAGJ1svYjEo5ve2Ssqx0=~-1~||0||~-1',
    # 'ak_bmsc': '66D32B455318BBCD2B767E9A72636E19~000000000000000000000000000000~YAAQ72+bG7dmI8mQAQAAqdZxzxjKz5tSDWKJhIaEKoAGwOE15+JM4zvUQpjFSljA16Q3EuEzxKTCIVdbbyOG/vjMDPUINSsIo9GVbDZMbgix936ladfnGNNasoyWJi7VgRbNnWXe0/MYs7Empx658Hl7QHQAJK95KH2dfijerX9Ys7aSyX25wQ7d+ebk4EYYzlFZKLcz0R8Ty2Ob+cHL71zxYN72ZyAjManXo58M1iNVTHYwGwPRzbaZ+4w8T5Km/50TKracVrIfPwKE7CZczMxkcd6rP3lL/vAcfy9sBPwBQiDu0ru955G8aZ7B+vu0e5LDDHcYLo7tz3VvsG1qqx3Yr1k3EqPxkzOryJKTJydXFCM499D04znVnbThhPbfmgFF5JkLP+Vz9WCn6LzYKxGM6qsSqqjm3BGu9S3C2ztQD1/0jzGn40m70qBUoTu0T7AWon6EtKPxbOPr4VZlJATXH8MCWEuVt4p4iyiJoUop',
    # 'bm_sv': '8399923DA47374F7B3E0B4CDD8767EF2~YAAQ72+bG/xmI8mQAQAAoANyzxgbDGKnwU+gemSR35UD8KScTaSWVvDheftc05ehOBIAuL3J1iZpawnLQjyHYnSClDH0GT2GTNmxNv0e2xXs1q70fAs/myzGAVTEclHVrlkbUjLeUArl81ftbodFaS9tQNHBJe2cy0/zcMcRxp0vh6xAUgp7DYXA1zSd/UUdgvRPbplh4t0QqByRta2+vVnnubqLn2kCakG8KFazQ8N2pHayNXw/7szLd1uq2/W9MJ8gNA==~1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': 'bm_sz=9CBE164C1A2C8E3CFC6AFD90A725B3EC~YAAQ72+bG6FmI8mQAQAAnM9xzxiOQa2FxeU0A8rUUL3pkw0EhTbRomvV6WrE0ETvGErhkTpxHXjuY+XqdhN0jqDqGwekvIk8v9TPBKS0QUPfIbSDIMECK0DVPo+TX8of3nt3BjV3Kn+Pp/3C+qZjGKi6XpYexzKy7pjJ5sz2Ketd26k3gTBFzupRjRinEwQnTDSe3IN1jajpfgFZPaem01Sa0VLakRIFp8ni0MtqFBmMqrbVh2yXSGNDpRKrDm71n6bN8bWK+GjtgoPSMinqPIc5CTSP8KwDi05or84Eqcqs7yQbkpecYH3l99rpGcVc/jHQgEhSPaelCql+pK5j2cJDt9xI1h1xuAhxr2yEOFY8oYZ2FtXEWQIybn9muBqjD/6/Dgr6MEdHKYo2ugd+8gTKUmkuV8MWpZpuudPsircTN151/w==~4601669~3355201; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22190cf71d06aab5-04d5a63df21805-26001f51-1382400-190cf71d06bbc8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkwY2Y3MWQwNmFhYjUtMDRkNWE2M2RmMjE4MDUtMjYwMDFmNTEtMTM4MjQwMC0xOTBjZjcxZDA2YmJjOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%7D; _abck=D37677AC859512A8EB74C93DA3AD3F23~0~YAAQ72+bG6xmI8mQAQAAP9Nxzwwo9pdx+eJLWKxFhIXqhrYpwO48pcx7cnSFA0CGN9muVve5NmbO7tGmabRAs39xvG2juk7PONFPK+0ycogVHmHp+3sTt9/5Y57dvpn8xFUwht+2WfzJk0OeFV7f+s5H25wDGbSrkbehlvWSNvgVK/d+Fhk30FeqkkPbsqjXoM4QSuDYo1Xl/wudcrvCDyxZ5ExKDVQLFjhN1sjMeoqW5ReRwBXyj5hClpn4yIJwDAq+b7oNo/nNyqbRGC5l2c5zaj48pxN7zIQ/AwAmHyonSveMCwNI9YolsNTEOPjMTPZUrHfw1iEHXVZ96y54xlW206lRcssmX1/ucXgl5IfrMfh89zTvj7zfHw7CyIrujbvS5rZRAibsNcpM36Zcf8iE9QIlvUfT6X3oLRM6+DupAsYNAGJ1svYjEo5ve2Ssqx0=~-1~||0||~-1; ak_bmsc=66D32B455318BBCD2B767E9A72636E19~000000000000000000000000000000~YAAQ72+bG7dmI8mQAQAAqdZxzxjKz5tSDWKJhIaEKoAGwOE15+JM4zvUQpjFSljA16Q3EuEzxKTCIVdbbyOG/vjMDPUINSsIo9GVbDZMbgix936ladfnGNNasoyWJi7VgRbNnWXe0/MYs7Empx658Hl7QHQAJK95KH2dfijerX9Ys7aSyX25wQ7d+ebk4EYYzlFZKLcz0R8Ty2Ob+cHL71zxYN72ZyAjManXo58M1iNVTHYwGwPRzbaZ+4w8T5Km/50TKracVrIfPwKE7CZczMxkcd6rP3lL/vAcfy9sBPwBQiDu0ru955G8aZ7B+vu0e5LDDHcYLo7tz3VvsG1qqx3Yr1k3EqPxkzOryJKTJydXFCM499D04znVnbThhPbfmgFF5JkLP+Vz9WCn6LzYKxGM6qsSqqjm3BGu9S3C2ztQD1/0jzGn40m70qBUoTu0T7AWon6EtKPxbOPr4VZlJATXH8MCWEuVt4p4iyiJoUop; bm_sv=8399923DA47374F7B3E0B4CDD8767EF2~YAAQ72+bG/xmI8mQAQAAoANyzxgbDGKnwU+gemSR35UD8KScTaSWVvDheftc05ehOBIAuL3J1iZpawnLQjyHYnSClDH0GT2GTNmxNv0e2xXs1q70fAs/myzGAVTEclHVrlkbUjLeUArl81ftbodFaS9tQNHBJe2cy0/zcMcRxp0vh6xAUgp7DYXA1zSd/UUdgvRPbplh4t0QqByRta2+vVnnubqLn2kCakG8KFazQ8N2pHayNXw/7szLd1uq2/W9MJ8gNA==~1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://www.adidas.com.cn/', cookies=cookies, headers=headers)
print(response.text)
