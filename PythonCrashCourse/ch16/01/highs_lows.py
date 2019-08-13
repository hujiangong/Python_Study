# -*- coding: utf-8 -*-
# @Time : 2019/8/13 14:50
# @Author : HuJiangong
# @File : highs_lows.py
# @Version : Python 3.6.4
# @Software: PyCharm
import csv
from matplotlib import pylab as plt
from datetime import datetime

# filename = 'sitka_weather_07-2014.csv'
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 返回list格式，处理以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
    # enumerate() 函数用于将一个可便利的数据对象（如列表、元祖或字符串）组合为一个索引列，同时列出数据和数据下标
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    # 使标题可以输出中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示符号

    plt.plot(dates, highs, c='red', alpha=0.5)  # alpha 设置透明度
    plt.plot(dates, lows, c='blue', alpha=0.5)  # 添加多条温度得执行多次plot()
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title('最高温度', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # 绘制倾斜的日期标签
    plt.ylabel('摄氏温度', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
