import re
import time
import random
import traceback
import requests

from selenium import webdriver


class Spider(object):
    '''
    微信公众号文章爬虫
    '''

    def __init__(self):
        # 微信公众号账号
        self.account = '286394973@qq.com'
        # 微信公众号密码
        self.pwd = 'lei4649861'

    def create_driver(self):
        '''
        初始化 webdriver
        '''
        options = webdriver.ChromeOptions()
        # 禁用gpu加速，防止出一些未知bug
        options.add_argument('--disable-gpu')

        # 这里我用 chromedriver 作为 webdriver
        # 可以去 http://chromedriver.chromium.org/downloads 下载你的chrome对应版本
        self.driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
        # 设置一个隐性等待 5s
        self.driver.implicitly_wait(5)

    def log(self, msg):
        '''
        格式化打印
        '''
        print('------ %s ------' % msg)

    def login(self):
        '''
        登录拿 cookies
        '''
        try:
            self.create_driver()
            # 访问微信公众平台
            self.driver.get('https://mp.weixin.qq.com/')
            # 等待网页加载完毕
            time.sleep(3)
            # 输入账号
            self.driver.find_element_by_xpath("./*//input[@name='account']").clear()
            self.driver.find_element_by_xpath("./*//input[@name='account']").send_keys(self.account)
            # 输入密码
            self.driver.find_element_by_xpath("./*//input[@name='password']").clear()
            self.driver.find_element_by_xpath("./*//input[@name='password']").send_keys(self.pwd)
            # 点击登录
            self.driver.find_elements_by_class_name('btn_login')[0].click()
            self.log("请拿手机扫码二维码登录公众号")
            # 等待手机扫描
            time.sleep(10)
            self.log("登录成功")
            # 获取cookies 然后保存到变量上，后面要用
            self.cookies = dict([[x['name'], x['value']] for x in self.driver.get_cookies()])

        except Exception as e:
            traceback.print_exc()
        finally:
            # 退出 chorme
            self.driver.quit()

    def get_article(self, query=''):
        try:
            url = 'https://mp.weixin.qq.com'
            # 设置headers
            headers = {
                "HOST": "mp.weixin.qq.com",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
            }
            # 登录之后的微信公众号首页url变化为：https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=1849751598，
            # 从这里获取token信息
            response = requests.get(url=url, cookies=self.cookies)
            token = re.findall(r'token=(\d+)', str(response.url))[0]
            time.sleep(2)

            self.log('正在查询[ %s ]相关公众号' % query)
            search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
            # 搜索微信公众号接口需要传入的参数，
            # 有三个变量：微信公众号token、随机数random、搜索的微信公众号名字
            params = {
                'action': 'search_biz',
                'token': token,
                'random': random.random(),
                'query': query,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'begin': '0',
                'count': '5'
            }
            # 打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
            response = requests.get(search_url, cookies=self.cookies, headers=headers, params=params)
            time.sleep(2)
            # 取搜索结果中的第一个公众号
            lists = response.json().get('list')[0]
            # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
            fakeid = lists.get('fakeid')
            nickname = lists.get('nickname')

            # 微信公众号文章接口地址
            search_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'

            # 搜索文章需要传入几个参数：登录的公众号token、要爬取文章的公众号fakeid、随机数random
            params = {
                'action': 'list_ex',
                'token': token,
                'random': random.random(),
                'fakeid': fakeid,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'begin': '0',  # 不同页，此参数变化，变化规则为每页加5
                'count': '5',
                'query': '',
                'type': '9'
            }
            self.log('正在查询公众号[ %s ]相关文章' % nickname)
            # 打开搜索的微信公众号文章列表页
            response = requests.get(search_url, cookies=self.cookies, headers=headers, params=params)
            time.sleep(2)
            for per in response.json().get('app_msg_list', []):
                print('title ---> %s' % per.get('title'))
                print('link ---> %s' % per.get('link'))
                # print('cover ---> %s' % per.get('cover'))

        except Exception as e:
            traceback.print_exc()


if __name__ == '__main__':
    spider = Spider()
    spider.login()
    spider.get_article('python')
