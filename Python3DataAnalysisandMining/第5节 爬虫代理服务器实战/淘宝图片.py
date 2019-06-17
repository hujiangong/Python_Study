import urllib.request
import re
shop='皮鞋'
shop_code=urllib.request.quote(shop)
page=0
url='https://s.taobao.com/search?q='+shop_code+'&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20171207&ie=utf8&bcoffset=4&ntoffset=4&p4ppushleft=1%2C48&s='+str(page)
print(url)
pat='"pic_url":"//(g-search\d.alicdn.com/.*?)"'
data=urllib.request.urlopen(url).read().decode('utf-8','ignore')
imageurlall=re.findall(pat,data)
# print(result)
i=0
# 还可以增加page参数获取更多页数的图片
for imageurl in imageurlall:
    imageurl='https://'+imageurl
    print(imageurl)
    file="taobaoimage/"+str(i)+'.jpg'
    try:
        urllib.request.urlretrieve(imageurl,file)
        print("第"+str(i)+"次爬取成功")
        i += 1
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print('第' + str(i) + '次爬取失败')
            print(e.code)
        if hasattr(e, "reason"):
            print('第' + str(i) + '次爬取失败')
            print(e.reason)
