import scrapy


class HospitalSpider(scrapy.Spider):
    name = 'hospital'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://z.xywy.com/']

    def parse(self, response):
        # 获取每个城市的链接
        city_list = response.xpath('//div[@class="z-area-table clearfix pt5"]/ul/li/a/@href').getall()
        for city_url in city_list:
            yield scrapy.Request(city_url, callback=self.parse_name)

    def parse_name(self, response):
        # 获取医院名和链接
        names = response.xpath('//ul[@class="clearfix"]/li/a/text()').getall()
        urls = response.xpath('//ul[@class="clearfix"]/li/a/@href').getall() 
        yield dict(zip(names, urls))

