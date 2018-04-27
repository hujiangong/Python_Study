import numpy
# 创建一维数组格式
# numpy.array([元素1,元素2,...,元素n])
x=numpy.array([1,22,3,7,3,11])


# 创建二维数组格式
# numpy.array([[元素1,元素2],...,[元素n,元素n+1]])
y=numpy.array([[121,2,32],[4,45,6],[711,83,9],[711,83,9]])
print(len(y))
#print(y)
# 排序
y.sort()
# print(y)
# 取最大值和最小值
y1=y.max()
print(y1)
# 切片
# 数组[起始下标:最终下标+1]
print(x[1:3])
print(x[:5])
print(x[2:])
