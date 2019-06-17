# -*- coding: utf-8 -*-
import scrapy
from Python3DataAnalysisandMining.第8节用Scrapy爬取网站的数据.dangdang.dangdang.items import DangdangItem
from scrapy.http import Request

class DangdSpider(scrapy.Spider):
    name = 'dangd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html']

    def parse(self, response):
        item = DangdangItem()
        # item["title"] = response.xpath("//a[class='pic']/@title").extract()
        item["title"] = response.xpath("//a[@class='pic']/@title").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        # return item
        yield item
        for i in range(2, 101):
            url = "http://category.dangdang.com/pg" + str(i) + "-cp01.54.06.00.00.00.html"
            yield Request(url=url, callback=self.parse)
