# -*- coding: utf-8 -*-
# @Time : 2018/4/2 10:33
# @Author : HuJiangong
# @File : append&extend.py
# @Version : Python 3.6.4
# @Software: PyCharm
import numpy as np
arrx=np.array([1,4,5,6,7])
arry=np.array([1.2,3.2,3.5,2.1,4.1])
cond=np.array([True,True,False,False,True])
# zipp=zip(arrx,arry,cond)
# for zippp in zipp:
#     print(zippp)
# print(zipp)
# happy=[]
# for x,y,c in zip(arrx,arry,cond):
#     happy.append(x if c else y)
#     # happy.extend(x if c else y)
happy = {x if c else y for x,y,c in zip(arrx,arry,cond)}
happy1 = {x if c else y for x,y,c in zip(arrx,arry,cond) if c==True }
print(type(happy))
print(happy)
print(happy1)
result=[a+1 for a in arrx if a!=5]
print(result)
for x,y,c in zip(arrx,arry,cond):
    if c:
        if c:
            x=c
        else:
            x=y
        happy=c
#     happy=[(x if c else y)]
#     print(happy)