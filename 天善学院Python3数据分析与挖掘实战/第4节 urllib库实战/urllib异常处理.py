import urllib.error
import urllib.request
try:
    urllib.request.urlopen("http://my.csdn.net/my/mycsdn")
    print("成功")
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)