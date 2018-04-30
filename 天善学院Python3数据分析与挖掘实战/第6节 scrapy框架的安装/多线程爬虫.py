# -*- coding: utf-8 -*-
# @Time : 2018/4/30 17:27
# @Author : HuJiangong
# @File : 多线程爬虫.py
# @Version : Python 3.6.5
# @Software: PyCharm


import urllib.request
import re
import time
import urllib.error
import threading


def use_proxy(url):
    # 建立异常处理机制
    try:
        req = urllib.request.Request(url)
        # 第一种方式，将浏览器模拟加到opener
        headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(req).read()
        time.sleep(1)
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
    except Exception as e:
        print("Exception:"+str(e))
        # 若为Exception 异常，延时1秒执行
        time.sleep(1)

class A(threading.Thread):
    def __init__(self,start_page):
        threading.Thread.__init__(self)
        self.start_page=start_page
    def run(self):
        for i in range(self.start_page, 10,2):
            thispageurl = "https://www.qiushibaike.com/8hr/page/" + str(i)
            thispagedata = use_proxy(thispageurl)
            thispagedata = thispagedata.decode("utf-8", "ignore")
            pat1 = r'<div class="content">.*?<span>(.*?)</span>'
            rs1 = re.compile(pat1, re.S).findall(str(thispagedata))

            if (len(rs1) == 0):
                print("第" + str(i) + "页没成功")
                continue
            for j in range(0, len(rs1)):
                print("第" + str(i) + "页第"+str(j)+"个段子成功")
                # print(rs1[j])
threadA=A(1)
threadA.start()
threadB=A(2)
threadB.start()

