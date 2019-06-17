#数组
a=['abc','def']
print(a)
#数组可以修改
a[0]='cde'
print(a)

#元祖
b=('edx','wsa')
print(b)
#元祖不可修改
#b[0]='eee'
#print(b)

#集合
#没有重复值
c='ienniknghixa'
#将c转换成集合
d=set(c)
print(d)
e='pmvcheq.kex.e'
f=set(e)
print(f)
#求交集
print(d&f)
#q求并集
print(d|f)

#字典
dict={'a':'aa','b':'bb'}
print(dict['a'])

# 迭代器
a = [1, 2, 3, 45]
print(type(a)) # <class 'list'>
print(a) # [1, 2, 3, 45] 直接输出list可以得到他的值
# 通过iter方法将一个list转换成迭代器
b = iter(a)
print(type(b)) # <class 'generator'>
print(b) # <list_iterator object at 0x021B8450>  直接输出迭代器

c=[d for d in a]
print(c) # <generator object <genexpr> at 0x001ED030>

#运算
#求商不要余数
print(4//3)

