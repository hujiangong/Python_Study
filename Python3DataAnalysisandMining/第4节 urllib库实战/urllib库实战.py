import urllib.request
# 直接下载整个网页
#urllib.request.urlretrieve("https://edu.hellobi.com/",filename='天善学院首页.html')
# 清理urlretrieve的缓存
#urllib.request.urlcleanup()
# 网站的一些信息
#file=urllib.request.urlopen("https://edu.hellobi.com/")
#print(file.info())
# 网页当前的状态码
#print(file.getcode())
# 网页当前的网址
#print(file.geturl())
# 设置超时时间
#file=urllib.request.urlopen("https://edu.hellobi.com/",timeout=0.01)

# Request()将一个网址转换成请求#
#keywd='奈戈岚勒'
## quote对中文进行编码
#keywd=urllib.request.quote(keywd)
#url='http://www.baidu.com/s?wd='+keywd+'&ie=utf-8&tn=baiduhome_pg'
#req=urllib.request.Request(url)
#data=urllib.request.urlopen(req).read()
#file=open(r'百度搜索.html','wb')
#file.write(data)
#file.close()

import urllib.parse
url='http://www.iqianyue.com/mypost/'
name='哈哈哈'
passwd='呵呵呵'
# quote()转码
#name=urllib.request.quote('哈哈哈')
#passwd=urllib.request.quote('呵呵呵')
heade=urllib.parse.urlencode({
    "name":name,
    "pass":passwd
}).encode('utf-8')
req=urllib.request.Request(url,data=heade)
# 直接读出来是byte类型
data=urllib.request.urlopen(req).read()
file=open(r'百度搜索2.html','wb')
file.write(data)
file.close()

