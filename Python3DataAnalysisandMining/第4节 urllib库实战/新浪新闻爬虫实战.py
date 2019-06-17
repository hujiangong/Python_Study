import urllib.request
import re
url='http://news.sina.com.cn/'
data=urllib.request.urlopen(url).read()
# 加第二个参数可以忽略错误
data=data.decode("utf-8","ignore")
pat='<a target="_blank" href="(http://news.sina.com.cn/.*?)"'
allurl=re.compile(pat).findall(data)
i=0
for thisUrl in allurl:
    try:
        print('第'+str(i)+'次爬取')
        urllib.request.urlretrieve(thisUrl, 'sinanew/' + str(i) + ".html")
        i += 1
        print("成功")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print('第' + str(i) + '次爬取失败')
            print(e.code)
        if hasattr(e, "reason"):
            print('第' + str(i) + '次爬取失败')
            print(e.reason)

