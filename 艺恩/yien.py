import execjs
import requests

url = 'https://www.endata.com.cn/API/GetData.ashx'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Origin': 'https://www.endata.com.cn',
    }

data = {
    'tdate': '2021-04-11',
    'MethodName': 'BoxOffice_GetHomeReleaseList'
}
# 加载出js文件
with open('webDES.min.js','r',encoding='utf-8') as f:
    js_data = f.read()
c = execjs.compile(js_data)

response = requests.post(url,headers=headers,data=data)
print(response.status_code)
s = response.text

# 调用js中的加密方法 shell
result = c.call('shell',s)
print(result)