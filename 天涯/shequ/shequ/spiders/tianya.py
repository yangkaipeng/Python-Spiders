import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import random
import json
from ..items import ShequItem

class TianyaSpider(CrawlSpider):
    name = 'tianya'
    # allowed_domains = ['www.tianya.com']
    sqitem = ShequItem()
    link = LinkExtractor(allow=r'/post.+shtml$')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )
    def start_requests(self):
        t = time.time()
        s = int(random.random()*1000)
        params = {
            'method': 'bbs.ice.getHotArticleList',
            'params.pageSize': 40,
            'params.pageNum': 2,
            'var': 'apiData',
            '_r': t,
            '_': s,         
        }
        url = 'https://bbs.tianya.cn/api'
        yield scrapy.Request(url, params=params, callback=self.parse)

    def parse(self,response):
        text = response.text[13:]
        data = json.loads(text).get('data').get('rows')
        urls = []
        for item in data:
            title = item.get('title')
            url = item.get('url')
            item['url'] = url
            item['title'] = title
            urls.append(url)
            yield item


    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
