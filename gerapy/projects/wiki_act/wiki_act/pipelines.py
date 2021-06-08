# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .items import WikiDirItem, WikiActItem

class WikiActPipeline(object):
    def open_spider(self, spider):
        self.f = open('name.txt', 'w', encoding='utf-8')
        self.f2 = open('dir_name.txt','w', encoding='utf-8')

    def process_item(self, item, spider):
        if isinstance(item, WikiDirItem):
            self.f2.write(item['name']+'\n')
        else:
            self.f.write(item['name']+'\n')
        return item

    def close_spider(self, spider):
        self.f.close()
        self.f2.close()