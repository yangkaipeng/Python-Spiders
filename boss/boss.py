import requests
requests.urllib3.disable_warnings()
from bs4 import BeautifulSoup
from lxml import etree
import re

cookies = {
    'lastCity':'101010100', 
    '__zp_seo_uuid__':'cb83b118-70e2-4aca-b8c2-42a5cfd76d75',
    '_bl_uid':'LFkbvnaw8LkyR5o329L9tw32vIbd', 
    '__g':'-', 
    'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a':'1617892623', 
    'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a':'1617892633', 
    '__fid':'29eb6eaa69537d31ec94b43b8bcc733c', 
    '__l':'r=https%3A%2F%2Fopen.weixin.qq.com%2F&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E5%2585%2589%25E5%25A4%25A7%25E8%25AF%2581%25E5%2588%25B8%26city%3D101010100%26industry%3D%26position%3D%26srcReferer%3Dhttps%3A%2F%2Fwww.zhipin.com%2F&s=3&g=&friend_source=0&s=3&friend_source=0', 
    '__c':'1617891196', 
    '__a':'41567122.1617891196..1617891196.31.1.31.31', 
    '__zp_stoken__':'2e3ccaTMMZyMhB3J1XjISSjlCfiUxbn07N1tLHy5KKVB%2BOHN7NCUiLjsscwRcLytzF3ZSLnUmUDh0OhNaK0JBCQV2FDdjaWo%2Fa0k%2BKgJzSjUuUhxENGc0Lm9FOUNBeGgJJ1VCNQ51VkgDClZ6'
    }

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
}

url = "https://www.zhipin.com/c101010100/?query=%E5%85%89%E5%A4%A7%E8%AF%81%E5%88%B8&page=1&ka=page-1"
res = requests.get(url,headers=headers,cookies=cookies,verify=False)

print(res.text)
li = re.findall('财富',res.text)
print(len(li))


html = BeautifulSoup(res.text,'lxml')
job_name=html.find_all('span',{'class':'job-name'})
for job in job_name:
    print(job)