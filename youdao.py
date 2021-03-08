import requests
import random
import time
import hashlib
import json

class YouDao:
    def __init__(self,word):
        self.word = word    # 要翻译的文本
        self.formdata = None    # 需要的传参
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"  # 实际发出的请求链接
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Cookie": "OUTFOX_SEARCH_USER_ID=1894454565@10.108.160.208; JSESSIONID=aaad-KV5kTKxWbvJYJ4Fx; OUTFOX_SEARCH_USER_ID_NCOO=984990548.44796; ___rl__test__cookies=1614782956571",
            "Referer": "http://fanyi.youdao.com/"
        }

    def generate_formdata(self):
        """
        根据分析js代码，得到加盐算法
            ts: "" + (new Date).getTime(),
            salt: ts+parseInt(10 * Math.random(), 10),
            sign: n.md5("fanyideskweb" + e + salt + "Tbh5E8=q6U3EXe+&L[4c@")

        """
        ts = str(int(time.time()*1000))
        salt = ts+str(random.randint(0,9))
        tempstr = "fanyideskweb" + self.word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        sign = hashlib.md5(tempstr.encode()).hexdigest()
        # 除以上三个参数为随机生成外，其他皆为固定值（2021年3月3日）
        self.formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": ts,
            "bv": "a03a283c42647ae8f9566bbe74f20922",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }

    def get_data(self):
        # 向此链接发送请求
        response = requests.post(self.url, data=self.formdata, headers=self.headers)
        data = response.content
        return data

    def run(self):
        # 生成参数
        self.generate_formdata()
        # 生成数据
        data = self.get_data().decode()
        data = json.loads(data)
        if data["errorCode"] == 0:
            tgt = data["translateResult"][0][0]["tgt"]
            print(tgt)
        

if __name__=="__main__":
    word = input('请输入您要翻译的中文：')
    yd = YouDao(word)
    yd.run()