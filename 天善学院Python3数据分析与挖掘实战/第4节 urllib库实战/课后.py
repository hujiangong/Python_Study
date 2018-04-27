import urllib.request
import re
url="http://blog.csdn.net/"
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
# 将opener添加为全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
# print(data)
pat='href="(http://blog.csdn.net/.*?)" target="_blank".*?</h2>'
result=re.findall(pat,data)
for i in range(0,len(result)):
    try:
        # print(result[i])
        urllib.request.urlretrieve(result[i], 'csdn/' + str(i) + '.html')
        # file=open('csdn/'+str(i)+'html','w')
        # file.write(urllib.request.urlretrieve(pat[i],'csdn/'+str(i)+'html'))
        print('第' + str(i) + '次爬取成功')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print('第' + str(i) + '次爬取失败')
            print(e.code)
        if hasattr(e, "reason"):
            print('第' + str(i) + '次爬取失败')
            print(e.reason)
