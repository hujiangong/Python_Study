import re
import urllib.request
# 读写2007 Excel
import openpyxl
data=urllib.request.urlopen("https://read.douban.com/provider/all").read()
data=data.decode('utf-8')
#print(str(data))
pat='<div class="name">(.*?)</div>'
resutl=re.compile(pat).findall(data)
i=0
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '豆瓣出版社'
print(len(resutl))
for cbs in resutl:
    print(cbs)
    i+=1
    sheet.cell(row=1,column=i, value=str(cbs))

    print('写入成功！')
wb.save('豆瓣出版社.xlsx')