# -*- coding: utf-8 -*-
import scrapy
from 

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        response.xpath("")
        # pass
import sys
print(sys.path)