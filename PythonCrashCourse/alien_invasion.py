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
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 设置窗口大小，(1200,800)是一个元组参数
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置窗口名称
    pygame.display.set_caption(("Alien Invasion"))

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()

    gf.creat_fleet(ai_settings, screen,ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # 让背景色填充屏幕，此方法只接受一个实参
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
