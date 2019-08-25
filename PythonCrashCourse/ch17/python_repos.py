# -*- coding: utf-8 -*-
# @Time : 2019/8/19 16:54
# @Author : HuJiangong
# @File : python_repos.py
# @Version : Python 3.6.4
# @Software: PyCharm

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code', r.status_code)

# 将API响应存储在一个变量中，返回 dict 格式
response_dict = r.json()
print(type(response_dict))
# exit()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print('\nKeys:',len(repo_dict))
# for key in repo_dict.keys():
#     print(key)
names, plot_dicts = [], []

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),  # 因为description在原文件里面有一个地方为空，所以需要转成字符串
        'xlink': repo_dict['html_url']  # Pygal 将根据与键'xlink'相关联的URL将每个条形都转换成活跃的链接
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45  # x轴倾斜45度
my_config.show_legend = False  # 隐藏图例
my_config.title_font_size = 24  # 图标标题
my_config.lable_font_size = 14  # 副标签 本例中不显示副标签？？
my_config.major_label_font_size = 18  # 主标签
my_config.truncate_label = 15  # 将较长的项目名阶段为15个字符
my_config.show_y_guides = False  # 隐藏图表中的水平线
my_config.width = 1000  # 自定义图标宽度

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
