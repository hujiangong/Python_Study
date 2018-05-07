#要想使用urlopen
# 第一种导入方式
from urllib.request import urlopen
data1=urlopen('http://www.baidu.com').read()
print(data1)

##第二种导入方式
import urllib.request
data2=urllib.request.urlopen('http://www.baidu.com').read()
print(data2)

#第三种导入方式
from urllib import request
data3=request.urlopen('http://www.baidu.com').read()
print(data3)

#D:\Program Files (x86)\Python\Python36-32\Lib下面自定义函数
import myfun
myfun.myfun()