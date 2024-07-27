# encoding: utf-8
"""
@author: The King
@project: JSProjects
@file: 测试数组变化.py
@time: 2024/7/21 19:48
"""


import requests

cookies = {
    '_ga': 'GA1.2.101968511.1721562332',
    '_ga_W5Z1BRK56L': 'GS1.2.1721562334.1.0.1721562334.0.0.0',
    'advertising_sharing_allowed': '{%22value%22:true}',
    'cb_dm': 'c9050b7f-e564-4e44-85e4-10283b5bc8a6',
    '__cf_bm': '70Pgl_SmBsp2VblddP7bZb_DXWPOYEpq3NH5vGrNb8M-1721562338-1.0.1.1-YmjAGaLQ.kNptiHPGRIKJVW0hWHiab5q.tPiRG8BtfrnNCNipleJsx7.4_xrXAXhGzzU5YvOgDo41gfjTgf4Ew',
    '_ga_90YJL6R0KZ': 'GS1.1.1721562331.1.0.1721562345.46.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,ko;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_ga=GA1.2.101968511.1721562332; _ga_W5Z1BRK56L=GS1.2.1721562334.1.0.1721562334.0.0.0; advertising_sharing_allowed={%22value%22:true}; cb_dm=c9050b7f-e564-4e44-85e4-10283b5bc8a6; __cf_bm=70Pgl_SmBsp2VblddP7bZb_DXWPOYEpq3NH5vGrNb8M-1721562338-1.0.1.1-YmjAGaLQ.kNptiHPGRIKJVW0hWHiab5q.tPiRG8BtfrnNCNipleJsx7.4_xrXAXhGzzU5YvOgDo41gfjTgf4Ew; _ga_90YJL6R0KZ=GS1.1.1721562331.1.0.1721562345.46.0.0',
    'origin': 'https://www.coinbase.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.coinbase.com/?__cf_chl_tk=LC59kZrdl0pVTZa1F2II2u2nyVClv8CaaleuLZA7E0A-1721562345-0.0.1.1-4287',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"126.0.6478.182"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

data = {
    '013dc426f7a4522f5590c64882c8b576bff22fedb927df2d2ef2a2fa2fe58581': 'puxhNHftr6SzETyl1Lu2fDcxI88_hwUlgxGVpz58Rto-1721562345-1.1.1.1-od463tJy1Sa0XxlB.poWFmpx0SnNI1Atjygvnq6YGuH8Y6fXREr6SiuGFbAjRb21oXUEpmPQ1BswowKn0k0S_JmdLnQxIRqIkFf71v2rdqXfSEyH6ZY3p04HlGUQ6Ml3x7YmVjDpxPLRaWLFaaJKyK5IK2nZHDOsVMTJxVFABscKM6q.Sq2RjbfyyiUHcPFJ5_NLHdnv1k7em1u7BxlPKr2z8USDsx4qE0S77S1ho97m32RKIxU70J3QWVYsEE3dEa7.nkbpd..V1rkw8H1J4bhH6U9xwjrwFHi.uxJZSg7kqlDhXMTllxUno5TxwABC3iWxwIY85ZN4ryIhMoNlTRkxL5Bmfx8kJ_zZzbzj8wvbJ78ylO6gUTNiYdzAaPwgFYnc3ZJAnfaApd7HFYPXrFB1CR7vyUBOanzj3kCoeMxzQiSFE6mESPEA.2sVVIybFlHh.p4fLGTMhptqSpy8fF07jvxkERp63wukJ2COE.VMleHerF1y_K5r14j.IX5gKqF9DGh0Ug6e5gQEo8Kz1Y2ZgYe0F83UDO8PXneyDibfBFwtKFlQ64u0xpbcJNByGdypmYp3yX4U2Vnx6XyZE.kcQrlirMMbJuF02kV17.fZJCeq5AbQNV_VBeSMAt2HUFKL3yJddu3iYUb8B90cZhZSxf8XwrRWK8wrXrBYgAuul5fyc86Zj0VRY0gx92KkSAxuVYiyhlJHD8_jAa2tPcbxVxWqZuQ2uejPoTj.wKkrhe8KVSp3B.dKXnMOP7n2sTD.CU1Ae_tafFYZtq_gOnKI20kJQBRQx82hgZImR3fqTJ20Jur2mDmxyu2sxV8bzpGw65IeSJS_H5pKuGWf_6EP2WSibMsaQAB_GAO0J4RYffqirnX0PGYHbhZ3k0I8.9zgy0r6.2d9z4cWy5Q1RF9WZaTqOoCoUf8op6_7zBAl3aA8K98KhelvdCw6tuGMinC.mfm9JXQ27WW6UB4OIk_Da8lvTDM4q3LA0qjY6cEWTQfSgsj2B_JyOPTfMjnVnua_07UtWxsXTZ5WQNVqnWtRPAJ8pTwLouuj6szsn0K0PHJKv6eTi4hVJ71btZluLYhsN8P64_rDrhDGB9J7zsaxdiGuhWAmetiWq62UfNzqKXAVLJgM6tVHs0xWoWg9dfybIesCdrbgZ5NHtJexSe_CtVJWhx7mMwoBAgpUILeQMTW30V3yQfBIZGiIcdyezZDXaA7HCMHZjLSupkGv6_hUsw26UOWtvapxcr8GUYqoQk.euBanl3s_o8zbskQQV7Yp2uRm1dK4foBqGq8o7AdZL0Zz_Jx2G9CfXFKAG8PJmuuTncoQqbzuS9nyjJg1HX0qw7YKZY0h_aa86sH_pariMRXy_Bsv4DA9UeDAj7ZEKjLyUIXoLVyzeQJJF8vAq9VvDi162mfo4hA3rww3Yg',
    '0a63603f8d03df8bbce020dc863b9712064272b14088db77aeb17e56e7a4fc69': 'USx5xSrKAUu2mI0G2F2zVoY8Kc_6AoCDHU3CioS5X7Y-1721562345-1.1.1.1-KD2XD521DyUgyoW6TWL3s5IWcAoK9U6NRLIntuKowef1R1KhuUQ6x4CdERNxjxzSHhMq.cjTMyS4tyWsKwE8gU0FAMyBnfptbc6sU_k6ZAFE8J.al7SArXx0KcccYtkXW5_Rpkikax.TgV9NcQp2a7vKVXYS8O.mS1e3Rnf9hMkmUlHrJAw4kKPqtglJ3SqTHctaSzUXsQSDP2XoO6TnHXkQ20yUtZ6ww88aRgO_j.MslEIZnsKrMqaPCbE09xy8ML1EXgq85Ztm5JhXhagBeFfPJyMyMY16SV_orVsgrkObw_74yympOyPhAFhCxclr5QUz5rGg7WPEEZF7hqhWUAsRtx3M9aaauqLrI95yzfCb9CMmnl8e3lU0KoebsVWs7i8wx.go1B_g_n7dMtpuCpnXiVHPus4fdUShVv.JpO6H_neqVNVTm3tySHWWaSTZ1xedRHDnK2jboPcCkF17wKcfgIXo2.68Jszg6sOn09up5dQ_PcjOeHfcvW6I6FgcoL9qv0.F0KdXPb0ctENWMvbky8vBcCFl6_OfnjNxfBHoe3qUBC.x5K8JuswFmwLZancBt7jaoy7.dfco5yfCSz1N_XsW7Ia.7VxEvlOseF3yrcSaZtIKKoF0eb1JXFNVNsuuLRhtvIFg4s3rOWl4qJl2z1QQWCfSl.7ozQZpVqaa_eA.h_3CjI9i4GTo6ZL2uHWKN9rAXKBUPa2Pw.3tGXIIJk8KPZyLMezUqXrhDTcexUULNLkATPE97Fif9sei4CQZTFaM7llRopBeON7FnQaIkzk6YBPLPCuAAKYehX6yCHIEFGeI8EEZ8ylTrW_XX.M5G4mbzu5IXsaIvmTeI7CfiN2aB3mmmdyBm8E9spx81qeNj_PhKnd_1Ff9mL9Df1ghhPVQA9wBj9mkDxWHDTlCS2p.D47y.115Uf8cMrJk7exx8jT1Iv2LqezQochBR2K8_WRukUsiTw4qsImSYXxvji_Wda_qH.vylcqI9lC5Tv0Vu4QrWhOkznRCj9NMuHV4OP4ibhWUHdcSXzbQom94DCQzmakjdm_cG76G0leq2VYOKhR0Icwu_nYOlEDyYESnUWM0M4WP7mr8WmNDAIOjdZ_shi19cLjqCNaZ.n10iJkqCbnHSPCLceGizDYvKmYQngjMEtLM4zC2jt3Aairc8ebgkOhau88T73mubOFEjqaNZ4DSlMfuEZdTN.plX5unAKSGqJvLQitnLVkEKEhD8eOCXuZlepQxzE0TkZEY2x_1.HKQOfDzHCRtTjsnSvyhia4Dt8AGq9Mu9xktJMVg8QWTnlMvf2qkenM_fXzl.3CZLWLDs8Fq4VYzGLhIRPdRi6ODa6Mdc0HO_jFHhWNZC6Z7G7LVeYNpXbYBFXtOMKvHyiEjiba3Q0IQokYL_od64SmKpYvGtJjxR1ffqDl2_vBvujeanRVUzQ..M1ijmjQem.P2jyQbdRphW68zX4FITjXmAhIceJbIxPiEPIcuAd_6UQySpx8YnVOi_OqcCYiyf3tXO5cD00wkaM19RxTWSyhgOW8CNhS.0NzJiaSlq1QrFlfJq47itg2DNvXTh_B09wqvhzHOFMo6S7S1RSRQqtWWu9Q70ejX9su3Zhfw9kCy.uMVoi_ovsKtaHvlN1ccAA4srLq31eZORL65QTI0OLUCD8uecUfnxkjRasCqA8jXzLuK8UWgsvtXvlKsb5Cu2XmWTT2wyovBEASLC48cTzUit5qFBiDGt9FFpAKHe8dTf0bLAEpptL_3caf6I_Kx1ZCoKNQR9gZAyjlJexwE7cYlxMymivpV1sla3OBS8mPZU4JpbY.aFlK08zNK1Nb2g.QEN.oZ8XT11zEFxJto7NLdxn8zBKLjpAnVs9cVukEzXu_KUFt98xQgHDneblqdJ6YnKsKjtvIxXPuqL09k2t02LdFZTHolwQbYyw.WuxKyOpp2jnD7FKKgsdfUoaDWbKzo1IfAwe54JQjH7e4XTEnaK7YDhT2J9HBbclmB68psKzomgFNDFOugvGVtOdxDljZ6j7zKCAoh2_LEJIoH3rLk338yPJVHJlxg8m6Ac_OeZNJybquz2vcd0osbzmndFPvbKOAM0YZJJCjXtx89E27bPLN3S0EQ9cLpPasUn_QgEQuILI_X4EcKWyHUMtA2e4_VLL02ShHHKWRA2crMmHzM69M2tz1VHNZygNnF1o3wJSfielDgboH.B4IOPfwvYnMtWuZWTNzJntmdx7meVAKvRZhivWbw4B249otOrDHtzWm3CAMIC96JxXEa8qpW9iCqOhvSR3BEm8mEqyzZN9M6xC0wFnGk.iiPMjKWKT1TfyFoQT1_7k1ItDUbPP83Lmo_PmJvaBL8fuTqBHxGQReRTa7RVp9XHHbZ4GP1Aeb6rGAmO7RficHJj0YOuNz.O.YBEAiPFc1jfR2EenA86QPLmCj0N_c.K5Uep03stgXFGlidG4hk5VITCNmSOz5SekZl1tRHJ9XbmDJ1WK7J12rWz2h0Lh4TNyKagIoy3A6z8A1Zy9yXeyopwHnKjEcdHi4ZxS67FbiGUOzqh5zw7XZ9Ehd4xFjTk270Epr8KaV5BVhfaJbFFFLk65VGO_z7scrtQbuSWvW3OvhPrxEs6R6WLFf3E.iBaYU7AlupZrl6.8bmf_LxSfoCUDC_O26QhJMAlDjX_XyNdnUuvadn_dpuGq47O_VOnjolGZlaCBP4w9rWib8ry_tk7XY',
    '06aa7746cfef2f766a215d3991253289b30ac3734fce97955cc36e57563221c7': '552f6aeea68bb45690164beac2ef3888',
    'b922042b61a681993ef4142ce1e5ad8ec259abadb14f256f9517e8f5f2d0de53': 'ZOtWtosrgorW-1-8a6af2560ffd96a5',
    '77f9e77f191bf1ae1d3bbeff9dbcbcc4048282a270a69e4b712bb6d8dff689ea': '69d3ab840f4a33579eabf98368d8b56b|{"managed_clearance":"ni"}',
}

response = requests.post('https://www.coinbase.com/', headers=headers, data=data)
print(response.text)


# 绕过
# 方法一  修改底层代码impersonate
from curl_cffi import requests as creq

c_resp = creq.post('https://www.coinbase.com/', headers=headers, data=data, impersonate="chrome101")
print(c_resp.text)
