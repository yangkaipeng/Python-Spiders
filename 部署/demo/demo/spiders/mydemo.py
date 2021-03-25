import scrapy


class MydemoSpider(scrapy.Spider):
    name = 'mydemo'
    # allowed_domains = ['www.demo.com']
    start_urls = ['http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml']

    def parse(self, response):
        print(response.url)
