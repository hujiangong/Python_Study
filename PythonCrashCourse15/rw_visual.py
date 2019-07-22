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
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input('再来一次？')
    if keep_running == 'n':
        break
