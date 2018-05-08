# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request

class DoubSpider(scrapy.Spider):
    name = 'doub'
    allowed_domains = ['douban.com']
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}

    # start_urls = ['http://www.douban.com/']

    def start_requests(self):
        # 这个地址是通过Fiddler抓包找到的。
        # 步骤可以使用登录豆瓣，估计输错密码。然后在发送的请求，可以找到这个地址。
        # 但是通过在豆瓣登录页面查看源代码找到的form表单的action地址是https://accounts.douban.com/login。可以确定豆瓣将真实的登录请求地址隐藏了
        print("start_requests")
        url = "https://www.douban.com/accounts/login"
        # meta开始cookie，才能在登录后保持登录状态
        yield Request(url=url, callback=self.parse, meta={"cookiejar": 1},headers=self.headers)

    def parse(self, response):
        captcha=response.xpath("//img[@id='captcha_image']/@src").extract()
        if len(captcha)>0:
            print("有驗證碼！")
            localpath="result/captcha.png"
            urllib.request.urlretrieve(captcha[0],localpath)
            print("请输入验证码")
            input=input()
            data = {
                "form_email": "15101151241",
                "form_password": "a1259068188",
                "redir":"https://www.douban.com/people/25690547/",
                "captcha-solution":str(input)
            }
            print("登录中......")
            return [FormRequest.from_response(response,formname="lzform",meta={"cookiejar": response.meta["cookiejar"]},
                                              headers=self.headers,
                                              formdata=data,
                                              callback=self.next,

                                              )]
        else:
            data = {
                "form_email": "15101151241",
                "form_password": "a1259068188",
                "redir":"https://www.douban.com/people/25690547/"
            }
            print("登录中......")
            return [FormRequest.from_response(response,formname="lzform",meta={"cookiejar": response.meta["cookiejar"]},
                                              headers=self.headers,
                                              formdata=data,
                                              callback=self.next,

                                              )]
    def next(self,response):
        print("success!")
        title = response.xpath("/html/dead/title/text()").extract()
        print(title)