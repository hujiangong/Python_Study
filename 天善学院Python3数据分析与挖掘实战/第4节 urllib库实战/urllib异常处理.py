import urllib.error
import urllib.request
# 在这有两种异常处理方式，详见同目录下 urllib库实战2 文本文件
try:
    urllib.request.urlopen("http://my.csdn.net/my/mycsdn")
    print("成功")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print('The server couldn\'t fulfill the request.')
        print(e.code)
    if hasattr(e,"reason"):
        print('We failed to reach a server.')
        print(e.reason)
