# -*- coding: utf-8 -*-
# @Time : 2019-06-16 10:55
# @Author : HuJiangong
# @File : alien_invasion.py
# @Version : Python 3.6.5
# @Software: PyCharm

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 设置窗口大小，(1200,800)是一个元组参数
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 设置窗口名称
    pygame.display.set_caption(("Alien Invasion"))

    # 创建一艘飞船
    ship = Ship(screen)

    # 设置背景颜色参数(灰色
    bg_color = (ai_settings.bg_color)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_event(ship)
        ship.update()
        # 让背景色填充屏幕，此方法只接受一个实参
        gf.update_screen(ai_settings,screen,ship)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
