import requests
import time
import random
from datetime import datetime
import json
from urllib import parse
import urllib3
urllib3.disable_warnings()

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Referer': 'https://xy2.cbgbook.com/goo.html',
}

url = 'https://xy2.cbgbook.com/goo/evaluate'

d_urls = []
with open(r'urls1.txt','r') as f:
    for detail_url in f.readlines():
        # print(detail_url.strip())
        # detail_url = 'https://xy2.cbg.163.com/equip?s=125&eid=202102081500213-125-NVWELHYLANX7&o&view_loc=overall_search'
        data = {
            'url':detail_url.strip()
        }
        try:
            response = requests.post(url, data=data, headers=headers, verify=False)
        except Exception as e:
            print(e)
            continue
        content = json.loads(response.text)
        code = content.get('code')
        if code == 0:
            info = content.get('info')
            roleInfo = info.get('roleInfo')
            totalPrice = info.get('totalPrice')
            old_price = float(roleInfo.split('￥')[-1])
            print(old_price,totalPrice)
            if totalPrice > old_price:
                d_urls.append(detail_url+'\n')
        time.sleep(random.random()*10)


if len(d_urls) > 0:
    with open(r'urls2.txt','w',encoding='utf-8') as f:
        f.writelines(d_urls)