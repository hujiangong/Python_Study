# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Python3DataAnalysisandMining.第7节scrapy爬虫.qsauto.qsauto.items import QsautoItem
from scrapy.http import Request

class QsbkSpider(CrawlSpider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # 自动爬虫的规则
    # 糗事百科所有的文章内容的链接都含有article，allow用的正则语法。callback是回调函数，默认是下面的parse_item,
    # follow 链接是否跟进，即爬了一个之后，是否还需要一层层继续爬下去。
    rules = (
        Rule(LinkExtractor(allow=r'article'), callback='parse_item', follow=True),
    )

    # 首次请求的模拟浏览器设置
    # 后续的模拟浏览器设置需要在settings中找到User-Agent设置
    def start_requests(self):
        ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        yield Request('http://www.qiushibaike.com/', headers=ua)

    def parse_item(self, response):
        i = QsautoItem()
        # 这里是自动爬取的详情页，爬取规则和直接在糗百首页爬取的规则不一样。注意改一下
        i["content"] = response.xpath("//div[@class='content']/text()").extract()
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()
        print(i['content'])
        print(i['link'])
        return i
