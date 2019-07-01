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

        self.ship_limit = 3

        # 外星人设置
        # 指定有外星人撞到屏幕边缘时，外星人群向下移动的速度。
        self.fleet_drop_speed = 10

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # 也可以写成 self.bullet_color = 60, 60, 60
        self.bullet_allowed = 10

        # 游戏升级设置
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 设置飞船的速度
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

    def  increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale