# -*- coding: utf-8 -*-
# @Time : 2019-06-16 11:14
# @Author : HuJiangong
# @File : settings.py
# @Version : Python 3.6.5
# @Software: PyCharm

class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 设置飞船的速度
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 也可以写成 self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
