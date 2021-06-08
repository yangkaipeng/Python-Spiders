import requests
import time
import random
import json


url = 'https://bbs.tianya.cn/api'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Referer': 'https://bbs.tianya.cn/',
    }

n = 0

while True:
    t = time.time()
    s = int(random.random()*1000)
    n += 1
    params = {
    'method': 'bbs.ice.getHotArticleList',
    'params.pageSize': 40,
    'params.pageNum': n,
    'var': 'apiData',
    # '_r': 0.6519208718619172,
    # '_': 1617204153630,
    '_r': t,
    '_': s,
    }   
    response = requests.post(url,headers=headers,params=params)
    if response.status_code == 200:
        text = response.text[13:]
        data = json.loads(text).get('data').get('rows')
        for item in data:
            print(item.get('title'))
            print(item.get('url'))
    elif n>3:
        break
