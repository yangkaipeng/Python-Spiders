#  通过Charles抓取到的参数，好像只是暂时能用


import requests
import random
from bs4 import BeautifulSoup
import json
import urllib3
urllib3.disable_warnings()


headers = {
    "user-agent":"Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.18(0x17001226) NetType/WIFI Language/zh_CN",
    "cookie":"devicetype=iPadiOS14.2;lang=zh_CN;pass_ticket=aQaV2H70N/bSbx2xDJirKAaGcOdVc/1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC;version=17001226;wap_sid2=CPCo9ucFEooBeV9ISWctb3ZNNWp0SXNtWkxKbFdUbnp4QVp0eVFuREhKaDNpRjV2cXF5ZEdXNGJQV1pKcHhadnFfdk1EbTNIeERza3FXM1pvdEpaRkZKUnVINjgyTThid2tNSzdTcjhjampkQnBKTXVYVGFFcW9GSS1LbkpUS0lhd2V5SEY0STBIRkNpMFNBQUF+MOSlnoIGOA1AlU4=;wxuin=1560122480"
}

urls = [
    # "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NDEzNTMyMA==&f=json&offset=10&count=10&is_ok=1&scene=&uin=777&key=777&pass_ticket=aQaV2H70N%2FbSbx2xDJirKAaGcOdVc%2F1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC&wxtoken=&appmsg_token=1103_UUm1tagxyCyIMZ0svdiZKchbAnwaNcrEKxN7GA~~&x5=0&f=json",
    # "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NDEzNTMyMA==&f=json&offset=10&count=10&is_ok=1&scene=&uin=777&key=777&pass_ticket=aQaV2H70N%2FbSbx2xDJirKAaGcOdVc%2F1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC&wxtoken=&appmsg_token=1103_nVEgE4pc6MfKNsMZSL2Cwk5z2RRmqdQNMeHq3A~~&x5=0&f=json",
    # "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NDEzNTMyMA==&f=json&offset=20&count=10&is_ok=1&scene=&uin=777&key=777&pass_ticket=aQaV2H70N%2FbSbx2xDJirKAaGcOdVc%2F1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC&wxtoken=&appmsg_token=1103_nVEgE4pc6MfKNsMZSL2Cwk5z2RRmqdQNMeHq3A~~&x5=0&f=json",
    # "https://mp.weixin.qq.com/mp/profile_ext?action=getmsg&__biz=MzA4NDEzNTMyMA==&f=json&offset=30&count=10&is_ok=1&scene=&uin=777&key=777&pass_ticket=aQaV2H70N%2FbSbx2xDJirKAaGcOdVc%2F1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC&wxtoken=&appmsg_token=1103_nVEgE4pc6MfKNsMZSL2Cwk5z2RRmqdQNMeHq3A~~&x5=0&f=json"
]

params = {
    "action": "getmsg",
    "__biz": "MzA4NDEzNTMyMA==",  # MjM5OTIxMzc4Mg==
    "f":"json",
    "offset": 40,
    "count": 10,
    "is_ok": 1,
    "scene":'',	
    "uin": 777,
    "key": 777,
    "pass_ticket":"aQaV2H70N/bSbx2xDJirKAaGcOdVc/1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC",  # aQaV2H70N/bSbx2xDJirKAaGcOdVc/1BJJYh46l3gLwJMDBLJsSyesMeegGbmabC
    "wxtoken":'',
    "appmsg_token": "1103_JCl7SefnVqWDLoTNGEqDjaCI1e1OzYnfwlC5QA~~",   # 1103_eTsEsReFGfJeqbwp4Ann_EUC1YquySFg3oovnQ~~
    "x5": 0,
    }

def get_html(url=None):
    url = 'https://mp.weixin.qq.com/mp/profile_ext'
    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        response.raise_for_status()
        html = BeautifulSoup(response.text, 'lxml')
        data = json.loads(html.find('p').text)
        if data and data['errmsg']== "ok":    # 反馈提示
            can_msg_continue = data['can_msg_continue']    # 是否还有下一页
            general_msg_list = data['general_msg_list']    # 具体内容
            general_msg_list = json.loads(general_msg_list)   # str -- json
            for content in general_msg_list['list']:
                title = content['app_msg_ext_info']['title']
                print(title)
    except Exception as e:
        print(e)

get_html()
