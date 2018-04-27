# -*- coding: utf-8 -*-
# @Time : 2018/3/6 11:52
# @Author : HuJiangong
# @File : sas.py
# @Version : Python 3.6.4
# @Software: PyCharm
from numpy import *
a=array([[1,0,0],[0,1,2],[2,0,0],[2,0,0]])
print(shape(a))
print (nonzero(a))
mat1=mat(a)
print('mat1:',type(mat1))
print('mat1.A:',type(mat1.A))
mean()