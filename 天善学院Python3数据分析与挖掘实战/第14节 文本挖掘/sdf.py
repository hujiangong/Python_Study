
# @Time : 2018/4/10 12:52
# @Author : HuJiangong
# @File : sdf.py
# @Version : Python 3.6.4
# @Software: PyCharm
# -*- coding: gbk -*-

import codecs

fileHandler = open('teset1.txt', mode='r', encoding='UTF-8')
report_lines = fileHandler.readlines()
filewrite=open('write.txt','a')
i=0
for line in report_lines:
    if i>10:
        break
    else:
        print(line)
        filewrite.write(line)
        i+=1
filewrite.close()

    # log = line.rstrip()
