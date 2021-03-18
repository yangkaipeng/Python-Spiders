import scrapy
from scrapy_redis.spiders import RedisSpider    # 导入这个类
from Hospital.items import HospitalItem
import re


class HospitalSpider(RedisSpider):    # 继承这个类
    name = 'hospital'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['http://z.xywy.com/']  # 注掉start_urls,
    redis_key = 'hospital:start_urls'     # 换成redis_key

    def parse(self, response):
        # 获取每个城市的链接
        city_list = response.xpath('//div[@class="z-area-table clearfix pt5"]/ul/li/a/@href').getall()
        for city_url in city_list:
        # city_url = city_list[0]
            yield scrapy.Request(city_url, callback=self.parse_name)

    def parse_name(self, response):
        # 获取医院名和链接
        item = HospitalItem()
        a = response.xpath('//ul[@class="clearfix"]/li/a').getall()
        for tag in a:
            name = re.findall('<a .*>(.*?)</a>',tag)[0]
            if name != '':
                url = re.findall('<a href="(.*?)"', tag)[0]
                print(name, url)
                item['name'] = name
                item['url'] = url
                yield item


