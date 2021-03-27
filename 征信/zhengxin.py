import requests
import random
import base64
import string
from user_agent import generate_user_agent
import time


# 验证码刷新过程
class ZhengXin:
    def __init__(self):
        self.captchaId = ''
        self.code = ''
        self.headers = {'User-Agent':generate_user_agent()}

    def get_captchaId(self):
        """
        分析js代码，获取关键参数
        """
        url = 'http://zxgk.court.gov.cn/shixin/captchaNew.do'
        chars = [i for i in string.digits+string.ascii_uppercase+string.ascii_lowercase]
        nums = ''.join(chars[int(random.random()*61)] for _ in range(32))
        self.captchaId = nums.replace('-','')
        r = random.random()
        params = {
            'captchaId':self.captchaId,
            'random':r
        }
        response = requests.get(url,headers=self.headers,params=params,verify=False)
        with open('code.png','wb') as f:
            f.write(response.content)
        # print(response.content)

    def get_code(self):
        """
        此处可调用第三方打码平台获取数据
        """
        return

    def send_code(self):
        """
        验证码是否正确的
        """
        url = 'http://zxgk.court.gov.cn/shixin/checkyzm.do'
        self.code = input('请代替超级鹰输入验证码:')
        params = {
            'captchaId':self.captchaId,
            'pCode':self.code
        }
        requests.get(url,headers=self.headers,params=params,verify=False)

    def search(self):
        """
        发送post请求
        """
        self.get_captchaId()
        self.send_code()
        url='http://zxgk.court.gov.cn/shixin/searchSX.do'
        pName = input('请输入要查找的人名:')
        data = {
            'pName': pName,
            'pCardNum':'', 
            'pProvince': 0,
            'pCode': self.code,
            'captchaId': self.captchaId,
            'currentPage': 1,
        }
        response = requests.post(url,headers=self.headers,data=data,verify=False)
        print(response.text)


zx = ZhengXin()
zx.search()
