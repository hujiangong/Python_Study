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

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned:', len(repo_dicts))

# 研究第一个仓库
# repo_dict = repo_dicts[0]
# print('\nKeys:',len(repo_dict))
# for key in repo_dict.keys():
#     print(key)
names, stars = [], []
for repo in repo_dicts:
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])

# 可视化
my_style = LS('#333366')
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 34

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')
