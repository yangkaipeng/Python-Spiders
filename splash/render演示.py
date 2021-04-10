import requests
from lxml import etree

# render.html端口
splash_url = 'http://0.0.0.0:8050/render.html'
args = {'url':'http://quotes.toscrape.com/js', 'timeout':'5', 'images':0}
res = requests.get(splash_url,params=args)
html = etree.HTML(res.text)
texts = html.xpath('//span[@class="text"]/text()')
for text in texts:
    print(text)



