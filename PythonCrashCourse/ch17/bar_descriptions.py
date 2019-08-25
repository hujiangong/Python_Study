# -*- coding: utf-8 -*-
# @Time : 2019-08-25 11:24
# @Author : HuJiangong
# @File : bar_descriptions.py
# @Version : Python 3.6.5
# @Software: PyCharm
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

'''
添加自定义工具提示
'''
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

# Pygal 根据与键"value"相关联的数字来确定条形的高度，并使用与'lable'相关联的字符串给条形图创建工具提示。注：必须是label
plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
