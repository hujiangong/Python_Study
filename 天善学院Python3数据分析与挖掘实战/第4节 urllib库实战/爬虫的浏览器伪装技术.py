import urllib.request
url="http://blog.csdn.net/qq_20745901/article/details/77096858"
headers=('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0')
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
#data=data.decode('gbk')
file=open('文件.txt','wb')
file.write(data)
file.close()
