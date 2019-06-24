# -*- coding: utf-8 -*-
# @Time : 2018/7/18 15:23
# @Author : HuJiangong
# @File : 字符串.py
# @Version : Python 3.6.4
# @Software: PyCharm

'''
字符串的基本操作
'''
S = 'A\nB\nC'
print(len(S))  # 5
S = ord('\n')
print(S)  # 10 输出字符的ASCII码，参数只能是一个字符
S = 'A\0B\0C'
print(len(S))  # 5 这里要注意 \x** 用2个16进制数表示一个字符 \***用3个8进制数表示一个字符  这里的\0 用的就是8进制的转义，不过是\000的缩写，高位的0可以省去。

'''
模式匹配
1、match
    re.match(pattern, string[, flags])  
从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。
第一次匹配成功就不再向后匹配。必须得是首字符开始就匹配

2、search
    re.search(pattern, string[, flags])  
若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个。

3、findall
    re.findall(pattern, string[, flags])  
返回string中所有与pattern相匹配的全部字串，返回形式为数组。

4、finditer
    re.finditer(pattern, string[, flags])  
返回string中所有与pattern相匹配的全部字串，返回形式为迭代器。

区别：
若匹配成功，match()/search()返回的是Match对象，finditer()返回的也是Match对象的迭代器，获取匹配结果需要调用Match对象的group()、groups或group(index)方法。
group()、groups()与group(index)的区别，如下所示：
'''
import re

s = '123abc456def789'
p = r'(\d*)([a-zA-Z]*)'
m = re.match(p, s)
print(m)
print(m.group())  # '123abc' group() 是可以最先可以匹配成功的第一个
print(m.group(0))  # '123abc' 同group()
print(m.group(1))  # 123  第一个括号匹配到的
print(m.group(2))  # abc  第二个括号匹配到的
print(m.groups())  # ('123', 'abc')

m = re.findall(p, s)
print(type(m))  # <class 'list'>
print(m)
# [('123', 'abc'), ('456', 'def'), ('', '')]
# 这里需要注意，如果模式为r'(\d*)([a-zA-Z]*)'，数组的最后一个值有('', '')，但是模式改为r'(\d+)([a-zA-Z]+)'，结果为[('123', 'abc'), ('456', 'def')]

p = r'(\d+)'
m = re.match(p, s)
print(m.group())  # 123
print(m.group(0))  # 123
print(m.group(1))  # 123
print(m.groups())  # ('123',)
m = re.findall(p, s)
print(m)  # ['123', '456', '789']

'''
综上：
group()：母串中与模式pattern匹配的子串；
group(0)：结果与group()一样；
groups()：所有group组成的一个元组，group(1)是与patttern中第一个group匹配成功的子串，group(2)是第二个，依次类推，如果index超了边界，抛出IndexError；
findall()：返回的就是所有groups的数组，就是group组成的元组的数组，母串中的这一撮组成一个元组，那一撮组成一个元组，这些元组共同构成一个list，就是findall()的返回结果。
           ！另，如果groups是只有一个元素的元组，findall的返回结果是子串的list，而不是元组的list了。
'''

# s ="1113446777"
# 用正则表达式把s分为1111, 3, 44, 6, 777

s = '1113446777'
m = re.findall(r'(\d)\1+', s)
# 这里的\1 这里理解。 如果匹配规则是(\d)(a-z)\1 这时候两个括号分别匹配，(\d)是第一个匹配，(a-z)是第二个匹配，这里的\1就是指第一个(\d),然后\1*就是指再次对匹配到的(\d)重复0次或多次，但是(\d)匹配到时1这里就是1，不能是别的数字
print(m)  # ['1', '3', '4', '6', '7']
# TODO  这里为什么加了\1以后输出的就是单个字符呢？
'''
m = re.findall(r'(\d)', s)
['1', '1', '1', '3', '4', '4', '6', '7', '7', '7']
'''
print('----------------------------')
s = '111aksdfksa4677ajds7'
m = re.search(r'(\d)+(a-z)+', s)
print('m',m)
print('m.group()',m.group())  # '111'
print('m.group(0)',m.group(0))  # '111'
print('m.group(1)',m.group(1))  # '111'
print('m.groups()',m.groups())  # ('1',)
'''
m = re.search(r'(\d)', s)
1
('1',)
'''
# ('1',)
# >>> m.group(0)
# '111'
# >>> m.group(1)
# '1'
# >>> m.group(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group
# >>> m=re.finditer(r'(\d)\1*',s)
# >>> m.next().group()
# '111'
# >>> m.next().group()
# '3'
# >>> m.next().group()
# '44'
# >>> m.next().group()
# '6'
# >>> m.next().group()
# '777'
# >>> m.next().group()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
#
# 另一个例子：
#
# >>> p = r'(\d)\1+([a-zA-Z]+)'
# >>> s = '1111werwrw3333rertert4444'
# >>> p = r'(\d)\1+([a-zA-Z]*)'
# >>> import re
# >>> re.findall(p,s)
# [('1', 'werwrw'), ('3', 'rertert'), ('4', '')]
# >>> m = re.search(p,s)
# >>> m.group()
# '1111werwrw'
# >>> m.group(1)
# '1'
# >>> m.group(2)
# 'werwrw'
# >>> m.groups()
# ('1', 'werwrw')
# >>> m = re.finditer(p,s)
# >>> m.next().group()
# '1111werwrw'
# >>> m.next().group()
# '3333rertert'
# >>> m.next().group()
# '4444'
# >>> m.next().group()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
