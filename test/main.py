import os
import requests
import time
import random

headers = {
    'authority': 'www.yhdmp.cc',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.yhdmp.cc/vp/21226-1-0.html',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ru;q=0.6',
    'cookie': f"t1={int(round(time.time() * 1000))}; t2={int(round(time.time() * 1000))+2000}; "
}

params = (
    ('aid', '21226'),
    ('playindex', '1'),
    ('epindex', '0'),
    ('r', str(random.random()))
)
print(params)
response = requests.get('https://www.yhdmp.cc/_getplay', headers=headers, params=params)
print(response.content.decode(encoding='utf-8',errors='ignore'))
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.yhdmp.cc/_getplay?aid=21226&playindex=1&epindex=0&r=0.0708871560710489', headers=headers)