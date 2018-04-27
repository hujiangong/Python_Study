# -*- coding: utf-8 -*-
# @Time : 2018/3/27 14:18
# @Author : HuJiangong
# @File : cumsum函数.py
# @Version : Python 3.6.4
# @Software: PyCharm
import numpy as np

arr = np.array([[[1, 2, 3], [8, 9, 12]], [[1, 2, 4], [2, 4, 5]]])
print(arr)
print(arr.shape)
print('----------------------')
print(arr.cumsum(0))
print('----------------------')
print(arr.cumsum(1))
print('----------------------')
print(arr.cumsum(2))