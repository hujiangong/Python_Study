# -*- coding: utf-8 -*-
# @Time : 2019-06-16 10:55
# @Author : HuJiangong
# @File : alien_invasion.py
# @Version : Python 3.6.5
# @Software: PyCharm

import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
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

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    aliens = Group()

    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 对编组aliens调用update()，这将自动对每个外星人调动方法update()
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # 让背景色填充屏幕，此方法只接受一个实参
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
