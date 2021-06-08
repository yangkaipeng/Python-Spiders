import requests
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
}

url = 'https://m.ixigua.com/api/feedv2/feedById'
params = {
    'aid': '3586',
    'timestamp': '1618737455789_172766.11864942694',
    'channelName':'', 
    'channelId': '94349555027',
    'count': '9',
    'refresh_type': 'open',
    'request_from': '710',
    'queryCount': '1',
    '_signature': '_02B4Z6wo00f01uK2znAAAIDA0uD55682VcbiosrAANjjH7yGfxCSX.Od6AJM.cJLmsJgEiHDwzlUTwJiUMecDwkZNfzgrP3b778u8bgZGp5DzmmI9YTI7v4UZTCkBBfsumwWsCb.Sz2PAS13b6',
}

res = requests.get(url,headers=headers, params=params, verify=False)
datas = json.loads(res.text)['data']['channel_feed']['data']
for data in datas:
    key = data['key']
    title = data['data']['title']
    print(title)
    print(key)
