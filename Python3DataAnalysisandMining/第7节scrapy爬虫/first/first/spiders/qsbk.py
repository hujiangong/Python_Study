# -*- coding: utf-8 -*-
import scrapy
from Python3DataAnalysisandMining.第7节scrapy爬虫.first.first.items import FirstItem
from scrapy.http import Request
class QsbkSpider(scrapy.Spider):
    # 糗百需要模拟浏览器
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    # start_urls 这是默认的首次爬取网页，如果使用模拟浏览器，需要自己重新设置
    # start_urls = ['http://www.qiushibaike.com/']

    def start_requests(self):
        ua={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        yield Request('http://www.qiushibaike.com/',headers=ua)
    def parse(self, response):
        it=FirstItem()
        # 糗百的内容
        it["content"]=response.xpath("//div[@class='content']/span/text()").extract()
        # 糗百的链接
        it["link"]=response.xpath("//a[@class='contentHerf']/@href").extract()
        yield it

