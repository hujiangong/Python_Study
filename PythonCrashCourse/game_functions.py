# -*- coding: utf-8 -*-
# @Time : 2019-06-16 21:16
# @Author : HuJiangong
# @File : game_functions.py
# @Version : Python 3.6.5
# @Software: PyCharm

import sys

import pygame


def check_event(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moveing_right = True
            elif event.key == pygame.K_LEFT:
                # 向左移动飞船
                ship.moveing_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moveing_right = False
            elif event.key == pygame.K_LEFT:
                ship.moveing_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
