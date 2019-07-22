# -*- coding: utf-8 -*-
# @Time : 2019-07-13 16:43
# @Author : HuJiangong
# @File : mpl_squares.py
# @Version : Python 3.6.5
# @Software: PyCharm

import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_value, squares, linewidth=5)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
