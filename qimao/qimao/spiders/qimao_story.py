import scrapy


class QimaoStorySpider(scrapy.Spider):
    name = 'qimao_story'
    # allowed_domains = ['www.qimao.com']
    start_urls = ['https://www.qimao.com/shuku/a-a-a-a-a-a-a-click-1/']

    def parse(self, response):
        print(response.xpath('/html/body/div[4]/div/div[2]/div/div[2]'))
