# -*- coding: utf-8 -*-
# @Time : 2019-07-22 23:17
# @Author : HuJiangong
# @File : rw_visual.py
# @Version : Python 3.6.5
# @Software: PyCharm

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
# 只要程序处于活动状态，就不断的模拟随机漫步
while True:

    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # 单位以英寸
    plt.figure(dpi=128, figsize=(12, 7))
    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', cmap=plt.cm.Blues, edgecolors='none', s=100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('再来一次？')
    if keep_running == 'n':
        break
