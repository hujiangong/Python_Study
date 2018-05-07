# -*- coding: utf-8 -*-
import scrapy
from Python3DataAnalysisandMining.第7节scrapy爬虫.first.first.items import FirstItem

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        item=FirstItem()
        item["content"]=response.xpath("/html/head/title/text()").extract()
        yield item # TODO 为什么会用yield
        # response.xpath("")
        # pass

# 这里要注意，测试的时候名字是你取的名字，也就是上面的name变量，而不是文件夹的名字
# scrapy crawl baidu --nolog