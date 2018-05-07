# -*- coding: utf-8 -*-
# @Time : 2018/3/20 14:02
# @Author : HuJiangong
# @File : 爬取腾讯视频短评.py
# @Version : Python 3.6.4
# @Software: PyCharm

"""
通过fiddler取到腾讯视频的短评链接：可以先打开一个视频，清空fiddler，然后点击更多短评，查看fiddler截取到的js文件，挨个打开找像短评的链接。
链接打开中文内容都是使用Unicode编码，可以在"输出Unicode编码.py"中输出和页面的短评对比一下。
爬取《乡村爱情10》的短评
首先通过fiddler抓到的第一页短评url为：
https://video.coral.qq.com/varticle/2483816022/comment/v2?callback=_varticle2483816022commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1521529184950
第二页短评为：
https://video.coral.qq.com/varticle/2483816022/comment/v2?callback=_varticle2483816022commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6379659716796832455&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1521529184953
观察可得有两个参数不一致，一个为cursor，一个为最后一个值。观察最后一个值可能为时间戳，所以最大可能为cursor。然后在第一页url中可以找到 "last" 的值观察为第二页短评中的 cursor 值，确定短评页数的参数为cursor
"""
import urllib.request
import re

class TencentMoive:
    # 初始化方法，定义一些变量
    def __init__(self):
        # 首页的cursor一般为0
        self.cursor = 0
        # 模拟浏览器
        self.headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
        # 创建opener，加入头代理
        self.opener = urllib.request.build_opener()
        self.opener.addheaders = [self.headers]
        # 将opener添加为全局
        urllib.request.install_opener(self.opener)

        # 存放段子的变量，每一个元素是每一页的段子们
        self.content_all = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getDate(self,cursor):
        try:
            # 连接参数合成请求url
            url = "https://video.coral.qq.com/varticle/2483816022/comment/v2?callback=_varticle2483816022commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(cursor)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1521529184950"
            # 发送请求，返回数据转换为utf-8编码
            data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
            # 返回页面内容
            return data
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                print("连接腾讯视频失败，错误原因：",e.reason)

    # 获取下一页的cursor即评论参数
    def getCursor(self,data):
        pat_last = r'"last":"(.*?)"'
        last_cursor = re.compile(pat_last).findall(data)
        return last_cursor[0]

    # 获取本页所有的短评内容
    def getComment(self,data):
        pat_content = r'"content":"(.*?)"'
        content_all = re.compile(pat_content).findall(data)
        comment=[]
        for content in content_all:
            comment.append(self.replaceEmoji(content))
        return comment

    # 替换Unicode中的emoji
    def replaceEmoji(self,comment):
        myre = re.compile(u'('
                          u'\ud83c[\udf00-\udfff]|'
                          u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                          u'\ud83e[\udc00-\ude4f\ude80-\udeff]|'
                          u'[\u2600-\u2B55])+',
                          re.UNICODE)
        return myre.sub('[Emoji]', comment.encode('latin-1').decode('unicode_escape'))

    # 开始方法
    def start(self):
        print (u"正在读取腾讯短视频,按回车查看新短评，Q退出")
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        data=self.getDate(self.cursor)
        self.content_all=self.getComment(data)

        while self.enable:
            print("进入了while循环")
            print(len(self.content_all) > 0)
            if len(self.content_all) > 0:
                for content in self.content_all:
                    # 等待用户输入
                    self.input = input()
                    # 如果输入Q则程序结束
                    if self.input == "Q":
                        self.enable = False
                        return
                    else:
                        print(content)
            print('新一页')
            new_cursor=self.getCursor(data)
            data = self.getDate(new_cursor)
            self.content_all = self.getComment(data)

test = TencentMoive()
test.start()
