a=111
b=(a)
print(b) # 不加逗号时表示强制转化，输出还是一个普通整型
b=(a,)
print(b) # 加逗号则表示转化成一个单元素的元组(111,)