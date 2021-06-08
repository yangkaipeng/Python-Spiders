import requests
import json
from lxml import etree

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}


url = "https://s.weibo.com/weibo/bixby?topnav=1&wvr=6&b=1"
response = requests.get(url, headers=headers)
# print(response.text)
html = etree.HTML(response.text)
# print(html)
card_wrap=html.xpath('//*[@id="pl_feedlist_index"]/div[1]/div[@class="card-wrap"]')
# print(card_wrap)
for card in card_wrap:
    txt = card.xpath('./div/div[1]/div[2]/p[@class="txt"]/text()')
    content = ''.join([i.strip() for i in txt])
    print(content)