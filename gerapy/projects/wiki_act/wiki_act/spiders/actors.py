# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import WikiActItem, WikiDirItem
import re

class ActorsSpider(scrapy.Spider):
    name = 'actors'
    # allowed_domains = ['www.en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Lists_of_actors','https://en.wikipedia.org/wiki/List_of_film_and_television_directors']
    items = WikiActItem()
    items_dir = WikiDirItem()
    pattern = 'List[s]* of'

    def parse(self, response):
        if 'directors' in response.url:
            names = response.xpath('//*[@id="mw-content-text"]/div[1]/div[@class="div-col"]/ul/li/a/text()').getall()
            for name in names:
                if '(' in name:
                    name = self.delData(name)
                if re.search(self.pattern, name):
                    continue
                self.items_dir['name'] = name
                yield self.items_dir
        else:
            urls = response.xpath('//*[@id="mw-content-text"]/div[1]/div[5]/ul/li/a/@href').getall()
            for href in urls:
                print(href)
                url = 'https://en.wikipedia.org'+href
                yield scrapy.Request(url, callback=self.parse_detail)


    def parse_detail(self, response):
        next_page = response.xpath('//*[@id="mw-pages"]/a[2]/@href').get()
        if next_page:
            names = response.xpath('//*[@id="mw-pages"]/div/div[@class="mw-category"]/div/ul/li/a/text()').getall()
            next_url = 'https://en.wikipedia.org'+next_page
            yield scrapy.Request(next_url, callback=self.parse_detail)
        else:
            content = response.xpath('//*[@id="mw-content-text"]/div[1]')
            name1 = content.xpath('./div[@class="div-col"]/ul/li/a/text()').getall()
            name2 = content.xpath('./ul/li/a/text()').getall()   # 
            url = response.url
            if name1:
                names = name1
            elif name2:
                names = name2
            elif 'Welsh' in url:
                names = response.xpath('//*[@id="mw-pages"]/div/div/div/ul/li/a/text()').getall()
            elif 'Czech' in url:
                names = response.xpath('//*[@id="mw-content-text"]/div[1]/div[3]/table/tbody/tr/td/ul/li/a/text()').getall()
            elif 'Vietnamese' in url:
                names = response.xpath('//*[@id="mw-content-text"]/div[1]/table/tbody/tr[2]/td[1]/a/text()').getall()
                if 'Name' in names:
                    names.remove('Name')
            elif 'Indonesian' in url:
                names = response.xpath('//*[@id="mw-pages"]/div/div/div/ul/li/a/text()').getall()
            elif 'Afghans' in url:
                names = response.xpath('//*[@id="mw-content-text"]/div[1]/div[13]/ul/li/a[1]/text()').getall()
            elif 'Bulgarian' in url:
                names = response.xpath('//*[@id="mw-content-text"]/div[1]/div[2]/table/tbody/tr/td/ul/li/a').getall()
            else:
                names = []
                print('错误链接:',response.url)
        for name in names:
            if 'List[s] of' in name:
                continue
            if re.search(self.pattern, name):
                continue
            if '(' in name:
                name = self.delData(name)
            self.items['name'] = name
            yield self.items
            # print(name)

    # 清理数据后面括号里的内容
    def delData(self, name):
        name = re.sub(r'\(.*','',name)
        return name

    
'''
https://en.wikipedia.org/wiki/List_of_Bulgarian_actors      //*[@id="mw-content-text"]/div[1]/div[2]/table/tbody/tr/td/ul/li/a

List of Chilean films
List of Chilean telenovelas    过滤掉

'''