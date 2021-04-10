import json
import requests


# 定义lua脚本，其中main为函数入口
lua_script = '''
function main(splash)
    splash:go("http://example.com")
    splash:wait(0.5)
    local title = splash:evaljs("document.title")
    return {title=title}
 end
 '''

# execute端口地址
splash_url = 'http://localhost:8050/execute'
headers = {'content-type':'application/json'}
data = json.dumps({'lua_source':lua_script})
response = requests.post(splash_url, headers=headers, data=data)
print(response.content)

