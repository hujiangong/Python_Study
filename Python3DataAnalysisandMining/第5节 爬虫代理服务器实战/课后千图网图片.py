import urllib.request
import re
import urllib.error
#page=1
#url="http://www.58pic.com/piccate/9-187-827-"+str(page)+".html"
#str='<img  src="http://img95.58pic.com/photo/00014/6026.jpg_wh860.jpg!w226?v=1" alt="ڵһ" width="290" height="437" height1="349.6" />'
#data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
# print(data)
# 问号前面的反斜杠是用来反义的
pat='(src=|data-original=)"(http://.*?)!w226\?v=1"'
#allimageurl=re.findall(pat,data)
i=0
for page in range(0,11):
    url = "http://www.58pic.com/piccate/9-187-827-" + str(page) + ".html"
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    allimageurl = re.findall(pat, data)
    for imageurl in allimageurl:
        try:
            urllib.request.urlretrieve(imageurl[1],"qiantuwangimage/"+str(i)+".jpg")
            i+=1
            #print(imageurl[1])
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print('第' + str(i) + '次爬取失败')
                print(e.code)
            if hasattr(e, "reason"):
                print('第' + str(i) + '次爬取失败')
                print(e.reason)
        except Exception as e1:
            print(e1)
