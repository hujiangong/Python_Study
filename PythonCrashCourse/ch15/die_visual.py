# -*- coding: utf-8 -*-
# @Time : 2019-07-25 22:47
# @Author : HuJiangong
# @File : die_visual.py
# @Version : Python 3.6.5
# @Software: PyCharm

import pygal
from ch15.die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die(10)
# 掷骰子，并将结果存储到一个列表中

results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()

hist.title = "两个6面骰子投1000次的结果"
hist.x_labels = list(range(2,17))
hist.x_title = "结果"
hist.y_title = "结果频率"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
