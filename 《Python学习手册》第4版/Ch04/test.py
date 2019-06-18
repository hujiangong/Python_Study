# -*- coding: utf-8 -*-
# @Time : 2018/7/18 18:27
# @Author : HuJiangong
# @File : test.py
# @Version : Python 3.6.4
# @Software: PyCharm
import re

s = '123aksd321fksa4677ajs7'
m = re.search(r'([\d]+)([a-z])+\1+', s)
print('m:', m)
print('m.group():', m.group())  # '111'
print('m.group(0):', m.group(0))  # '111'
print('m.group(1):', m.group(1))  # '111'
print('m.group(2):', m.group(2))  # '111'
print('m.groups():', m.groups())  # ('1',)

s = 'abcdef4677ghijklmn'
m = re.match(r'([a-z])+?', s)
print('m.group(1):', m.group(1))  # f

