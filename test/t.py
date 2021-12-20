import requests
import random
import math
import time

se=requests.Session()
ads={
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
    }
se.headers.update(ads)
res=se.get('https://www.yhdmp.cc/vp/21226-1-0.html')
t1=int(se.cookies.get_dict()['t1'])
k2=math.floor(round(t1/1000)/32)
k2=(k2 * (k2 % 4096) + 39382) * (k2 % 4096) + k2
se.cookies.set('k2',str(k2))
se.cookies.set('t2',str(int(round(time.time() * 1000))))

#print(se.headers)

#print(se.cookies.get_dict())
res=se.get(f'https://www.yhdmp.cc/_getplay?aid=21226&playindex=1&epindex=0&r={random.random()}')

print(res.content.decode(encoding='utf-8',errors='ignore'))