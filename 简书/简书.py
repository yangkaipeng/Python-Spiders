import requests
import time
import random
import csv
import codecs
from user_agent import generate_user_agent
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()


class JianShu:
    def __init__(self):
        self.user_agent = generate_user_agent()
        self.url = 'https://www.jianshu.com/'
        self.session = requests.session()
        self.token = None
        self.ids = []
    
    def get_token(self):
        """
            从返回界面中找到csrf_token
        """
        headers = {'User-Agent':self.user_agent}
        try:
            response = self.session.get(self.url, headers=headers, verify=False)
            html = BeautifulSoup(response.text,'lxml')
            self.get_ids(html)
            self.token = html.find('meta',{'name':'csrf-token'}).get('content')   
        except Exception as e:
            print(e) 
    
    def get_ids(self, html):
        """
            获得参数中所需要的seen_snote_ids[]
        """
        ids = []
        div = html.find('div',{'id':'list-container'})
        for li in div.find_all('li'):
            id = li.get('data-note-id')
            ids.append(id)
        self.ids = ids

    def get_content(self):
        """
         获得主要的数据，
         观察xhr文件，构建headers和params中的必须参数
        """
        self.get_token()
        content = []
        for page in range(2, 10):
            headers = {
                'User-Agent':generate_user_agent(),
                'X-CSRF-Token':self.token,
                'X-INFINITESCROLL': 'true',
                'X-Requested-With': 'XMLHttpRequest'
            }
            params = {
                'page':page,
                'seen_snote_ids[]':self.ids
            }
            time.sleep(random.random()*5)
            try:
                response = self.session.get(self.url, headers=headers, params=params, verify=False)
                response.raise_for_status()
                html = BeautifulSoup(response.text, 'lxml')
                for li in html.find_all('li'):
                    title = li.find('a',{'class':'title'}).text.strip()
                    abstract = li.find('p',{'class':'abstract'}).text.strip()
                    data_note_id = li.get('data-note-id')
                    content.append({'id':data_note_id,'title':title,'abstract':abstract})
            except Exception as e:
                print(e)
        self.save_csv(content)

    def save_csv(self, content):
        """
            保存到csv文件中
        """
        headers = ['id', 'title', 'abstract']
        try:
            with codecs.open(r'./jianshu.csv','a','utf-8') as fp:
                f_csv = csv.DictWriter(fp, fieldnames=headers)
                f_csv.writeheader()
                f_csv.writerows(content)
        except Exception as e:
            print(e)
            

if __name__=="__main__":
    js = JianShu()
    js.get_content()