import requests
from user_agent import generate_user_agent
import json
import time

class TouTiao:
    def __init__(self):
        self.headers = {'User-Agent':generate_user_agent()}
        self.url = 'https://www.toutiao.com/api/pc/feed/'
        self.params = {      # 这些均为固定参数
            'category':'news_hot',
            'utm_source':'toutiao',
            'widen':1,
            'tadrequire':'true'
        }
        self.max_behot_time = ''    # 每次需在上一个回复中获得

    def first_get(self):
        params = self.params
        params['min_behot_time'] = 0
        response = requests.get(self.url,params=params,headers=self.headers)
        pre = json.loads(response.text)
        self.max_behot_time = pre['next']['max_behot_time']
        print(self.max_behot_time)
        for data in pre['data']:
            print(data['title'])

    def next_get(self):
        params = self.params
        params['max_behot_time'] = self.max_behot_time
        print(params['max_behot_time'])
        response = requests.get(self.url,params=params,headers=self.headers)
        pre = json.loads(response.text)
        self.max_behot_time = pre['next']['max_behot_time']
        for data in pre['data']:
            print(data['title'])

tt = TouTiao()
tt.first_get()
for i in range(5):
    time.sleep(2)
    tt.next_get()