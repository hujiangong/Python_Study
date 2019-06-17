# -*- coding: utf-8 -*-
# @Time : 2018/4/30 10:43
# @Author : HuJiangong
# @File : 微信爬虫实战.py
# @Version : Python 3.6.5
# @Software: PyCharm

import urllib.request
import re
import time
import urllib.error


def use_proxy(proxy_addr, url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        # 第一种方式，将浏览器模拟加到opener
        headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        # 第二种方式 直接将浏览器模拟加到request中
        # req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        proxy = urllib.request.ProxyHandler({'http': proxy_addr})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        # opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print('The server couldn\'t fulfill the request.')
            print(e.code)
        if hasattr(e, "reason"):
            print('We failed to reach a server.')
            print(e.reason)
        # 若为URLError异常，延时10秒执行
        time.sleep(10)
    # except Exception as e:
    #     print("Exception:"+str(e))
    #     # 若为Exception 异常，延时1秒执行
    #     time.sleep(1)

#设置关键词
key="Python"
#设置代理服务器。一般免费的都不太好使，知道即可
proxy="123.56.89.238:60443"
#爬多少页
for i in range(10):
    ## quote对中文进行编码
    key=urllib.request.quote(key)
    thispageurl="http://weixin.sogou.com/weixin?query="+key+"&_sug_type_=&sut=882&lkt=1%2C1525058402138%2C1525058402138&s_from=input&_sug_=y&type=2&sst0=1525058402240&page="+str(i)+"&ie=utf8&w=01019900&dr=1"
    print(thispageurl)
    thispagedata=use_proxy(proxy,thispageurl)
    pat1=r'<h3>.*?<a target="_blank" href="(.*?)"'
    rs1=re.compile(pat1,re.S).findall(str(thispagedata))
    if(len(rs1)==0):
        print("第"+str(i)+"页没成功")
        continue
    for j in range(0,len(rs1)):
        thisurl=rs1[j]
        thisurl=thisurl.replace("amp;","")
        print(thisurl)
        file="weixinhtml/第"+str(i)+"页第"+str(j)+"篇文章.html"
        thisdata=use_proxy(proxy,thisurl)
        try:
            fh=open(file,"wb")
            fh.write(thisdata)
            fh.close()
            print("第"+str(i)+"页第"+str(j)+"篇文章爬取成功")
        except urllib.error.URLError as e:
            print("第" + str(i) + "页第" + str(j) + "篇文章爬取失败")
            if hasattr(e, "code"):
                print('The server couldn\'t fulfill the request.')
                print(e.code)
            if hasattr(e, "reason"):
                print('We failed to reach a server.')
                print(e.reason)
