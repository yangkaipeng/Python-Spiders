import requests
import time
import random
from datetime import datetime
import json
from urllib import parse
import urllib3
urllib3.disable_warnings()


def get_url():
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Referer': 'https://xy2.cbg.163.com/cgi-bin/equipquery.py?act=show_overall_search',
    }

    url = 'https://xy2.cbg.163.com/cgi-bin/search.py'
    detail_urls = []
    for page in range(1,101):
        rand = datetime.now().strftime('%a %b %d %Y %H:%M:%S')+' GMT+0800 (中国标准时间)'
        # 'Sat May 08 2021 22:23:45 GMT+0800 (中国标准时间)'
        params = {
            'act': 'overall_search_role',
            'page': page,
            'price_max': '1000000',
            'price_min': '300000',
            'server_type': '3',
            'random': rand,
        }
        try:
            response = requests.get(url, headers=headers,params=params, verify=False)
        except Exception as e:
            print(e)
            continue
        try:
            content = json.loads(response.text)
        except:
            print('IP被封了')
            break
        msg=content.get('msg')
        for m in msg:
            equip_name = m.get('equip_name',None)
            eid = m.get('eid')
            s = m.get('serverid')
            price = m.get('price')
            data = {
                's': s,
                'eid': eid,
                'o': '', 
                'view_loc': 'overall_search'
            }
            d = parse.urlencode(data)
            detail_url = f'https://xy2.cbg.163.com/equip?{d}'
            if bijia(detail_url):
                detail_urls.append(detail_url+'\n')
        time.sleep(random.random()*10)
    if len(detail_urls) > 0:
        with open(r'urls.txt','w',encoding='utf-8') as f:
            f.writelines(detail_urls)

def bijia(detail_url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Referer': 'https://xy2.cbgbook.com/goo.html',
    }
    url = 'https://xy2.cbgbook.com/goo/evaluate'
    data = {
        'url':detail_url.strip()
        }
    try:
        response = requests.post(url, data=data, headers=headers, verify=False)
    except Exception as e:
        print(e)
    content = json.loads(response.text)
    code = content.get('code')
    if code == 0:
        info = content.get('info')
        roleInfo = info.get('roleInfo')
        totalPrice = info.get('totalPrice')
        old_price = float(roleInfo.split('￥')[-1])
        print(old_price,totalPrice)
        if totalPrice > old_price:
            return True
    return False


get_url()