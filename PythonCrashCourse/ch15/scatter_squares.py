# -*- coding: utf-8 -*-
# @Time : 2019-07-13 16:57
# @Author : HuJiangong
# @File : scatter_squares.py
# @Version : Python 3.6.5
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]
# c 为点的颜色，edgecolors 为点轮廓颜色 ： c 有两种写法，或者为'red'文本，或者单行的二维数据
# 注：c 不建议直接传RGB元祖，会提示"'c' argument looks like a single numeric RGB or RGBA sequence, which should be avoided as value-mapping will have precedence in case its length matches with 'x' & 'y'.  Please use a 2-D array with a single row if you really want to specify the same RGB or RGBA value for all points."
# c = numpy.array([[0, 1, 0.8]])
# plt.scatter(x_value, y_value, c=c, edgecolors='none', s=40)

# 从起始颜色渐变到结束颜色，较浅的颜色表示较小的值，较深的颜色显示较大的值。
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

# 注意，如果show()在savefig()前面的话，保存的图片就是空白
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()