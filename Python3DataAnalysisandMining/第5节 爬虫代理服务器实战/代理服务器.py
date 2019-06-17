# 本代码没生效
import urllib.request
def use_proxy():
    proxy=urllib.request.ProxyHandler({"http:":"149.81.248.105:8111"})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    #urllib.request.install_opener(opener)
    data =opener.open('http://blog.csdn.net/qq_20745901/article/details/77096858').read()
    #data = urllib.request.urlopen('http://blog.csdn.net/qq_20745901/article/details/77096858').read()
    data = data.decode('utf-8')
    print(data)

use_proxy()
