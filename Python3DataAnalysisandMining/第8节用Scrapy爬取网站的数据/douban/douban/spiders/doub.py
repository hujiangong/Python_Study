# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request

class DoubSpider(scrapy.Spider):
    name = 'doub'
    allowed_domains = ['douban.com']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}

    # start_urls = ['http://www.douban.com/']

    def start_requests(self):
        # 这个地址是通过Fiddler抓包找到的。
        # 步骤可以使用登录豆瓣，估计输错密码。然后在发送的请求，可以找到这个地址。
        #  在页面源代码中找到的form表单的action地址也是这个，但有些反爬机制比较高的网站可能不一样
        url = "https://accounts.douban.com/login"
        # meta开始cookie，才能在登录后保持登录状态
        return [Request(url=url, callback=self.parse, meta={"cookiejar": 1}, headers=self.headers)]

    def parse(self, response):
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        if len(captcha) > 0:
            print("有驗證碼！")
            localpath = "result/captcha.png"
            urllib.request.urlretrieve(captcha[0], localpath)
            print("请输入验证码")
            captcha_value = input()
            data = {
                "form_email": "15101151241",
                "form_password": "a1259068188",
                "redir": "https://www.douban.com/people/25690547/",
                "captcha-solution": captcha_value
            }
        else:
            data = {
                "form_email": "15101151241",
                "form_password": "a1259068188",
                "redir": "https://www.douban.com/people/25690547/"
            }
        print("登录中......")
        return [FormRequest.from_response(response, meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.headers,
                                          formdata=data,
                                          callback=self.next,
                                          )]

    def next(self, response):
        print("success!")
        title = response.xpath("/html/head/title/text()").extract()
        print(title[0])
