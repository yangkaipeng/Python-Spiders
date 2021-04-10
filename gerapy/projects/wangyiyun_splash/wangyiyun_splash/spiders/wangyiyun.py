# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class WangyiyunSpider(scrapy.Spider):
    name = 'wangyiyun'
    # allowed_domains = ['https://news.163.com/domestic/']
    start_urls = ['https://news.163.com/domestic//',
                    'https://news.163.com/world/',
                    'https://war.163.com/']
    def start_requests(self):
        for url in self.start_urls:
            # 先加载url，然后操作页面下滑scrollTo，到出现“加载更多”按钮后，点击。直到出现“已经到最后啦”，返回html
            script = """
                function main(splash)
                  splash.images_enabled=false
                  assert(splash:go(splash.args.url))
                  local scroll_to = splash:jsfunc("window.scrollTo")
                  local height = splash:jsfunc("function() {return document.body.scrollHeight;}")
                  repeat
                    scroll_to(0, height())
                    load_more_btn = splash:select("a[class='load_more_btn'][style='display: block;']")
                    load_more_tip = splash:select("div[class='load_more_tip'][style='display: block;']")
                    if load_more_btn~=nil then
                      load_more_btn.mouse_click()
                    end
                    splash:wait(0.5)
                  until load_more_tip ~= nil
                  splash:wait(1)
                  return {html=splash:html()}
                end  
            """
            yield SplashRequest(url,args={'timeout': 15,'lua_source': script},endpoint="execute")
            

    def parse(self, response):
        news_type = response.xpath('//div[@class="ns_area hd"]//strong/text()').get()
        ndi_main = response.xpath('//div[@class="data_row news_article clearfix "]')
        print(news_type+'新闻总数：',len(ndi_main))
        for article in ndi_main:
            title = article.xpath('.//h3/a/text()').get()
            url = article.xpath('.//h3/a/@href').get()
            print('标题：',title)
            print('url',url)

