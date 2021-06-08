# from scrapy import cmdline

# cmdline.execute('scrapy crawl qimao_story'.split())
from lxml import etree
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup

import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
params = {
    'dqs': '010',
    'searchType': 1,
    'degradeFlag': 0,
    'sortFlag': 15,
    'd_headId': '9a694632e4d557fbb05acba4fe03f890',
    'd_ckId': 'f5938f92583efdac49998523ef881154',
    'd_sfrom': 'search_fp',
    'd_curPage': 0,
    'd_pageSize': 40,
    'siTag': 'tF7woi2y6F2s2RnHW3wfUw~F5FSJAXvyHmQyODXqGxdVw',
    'key': 'python爬虫',
    # 'curPage':0
}

response = requests.get('https://www.liepin.com/zhaopin/',headers=headers,verify=False,params=params)
# print(response.text)
# html = etree.HTML(response.text)
# sojob_list = html.xpath('//*[@class="sojob-result"]')
# print(sojob_list)
# for job in sojob_list:
#     title = job.xpath('./div[@class="job-info"]/h3/text()')
#     print(title)
 

soup = BeautifulSoup(response.text,'lxml')

result = soup.find('ul',{'class':'sojob-list'})
for job_info in result.find_all('li'):
    print(job_info.find('h3').text.strip())
    print(job_info.find('p',{'class':'company-name'}).text.strip())
# print(result)
""" 
dqs: 010
pageSize: 40
sortFlag: 15
degradeFlag: 0
key: python爬虫
siTag: tF7woi2y6F2s2RnHW3wfUw~F5FSJAXvyHmQyODXqGxdVw
d_sfrom: search_fp
d_ckId: f5938f92583efdac49998523ef881154
d_curPage: 1
d_pageSize: 40
d_headId: 9a694632e4d557fbb05acba4fe03f890
curPage: 2
"""

""" 
    dqs: 010     不变
    pageSize: 40   
    sortFlag: 15   不变
    degradeFlag: 0    
    key: python爬虫   不变
    siTag: tF7woi2y6F2s2RnHW3wfUw~F5FSJAXvyHmQyODXqGxdVw   一样
    d_sfrom: search_fp    不变
    d_ckId: f5938f92583efdac49998523ef881154   不变
    d_curPage: 0
    d_pageSize: 40
    d_headId: 9a694632e4d557fbb05acba4fe03f890
    curPage: 1
"""

"""
dqs: 010
pageSize: 40
sortFlag: 15
degradeFlag: 0
key: python爬虫
siTag: tF7woi2y6F2s2RnHW3wfUw~F5FSJAXvyHmQyODXqGxdVw
d_sfrom: search_fp
d_ckId: f5938f92583efdac49998523ef881154
d_curPage: 1
d_pageSize: 40
d_headId: 9a694632e4d557fbb05acba4fe03f890
curPage: 2
"""