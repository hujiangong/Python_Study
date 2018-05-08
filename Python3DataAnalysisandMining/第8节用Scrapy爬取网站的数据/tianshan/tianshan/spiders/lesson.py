# -*- coding: utf-8 -*-
import scrapy
from Python3DataAnalysisandMining.第8节用Scrapy爬取网站的数据.tianshan.tianshan.items import TianshanItem
from scrapy.http import Request

class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['http://edu.hellobi.com/course/280']

    def parse(self, response):
        item = TianshanItem()
        # 这里是自动爬取的详情页，爬取规则和直接在糗百首页爬取的规则不一样。注意改一下
        item["title"] = response.xpath("//div[@class='course-info']/h1/text()").extract()
        item["link"] = response.xpath("//input[@name='redirect_url']/@value").extract()
        item["stu"] = response.xpath("//span[@class='course-view']/text()").extract()
        # 这里注意一下价格！！！ 在登录状态和非登录状态查看源代码看到的价格是不一样的。而且，打折的课程和免费的课程价格也是不一样的，所以，这里的价格是不能这么爬取的。
        # item["price"]=response.xpath("//strong[@class='money']/text()").extract()
        yield item
        # for j in range(1,281):
        for j in range(1, 3):
            url = 'https://edu.hellobi.com/course/' + str(j)
            # 注意！！ 这里的callback赋予的是方法名，不是方法，也就是不可以写self.parse()
            yield Request(url, callback=self.parse)
