# -*- coding: utf-8 -*-
# @Time : 2019-06-16 17:28
# @Author : HuJiangong
# @File : ship.py
# @Version : Python 3.6.5
# @Software: PyCharm

import pygame
from settings import Settings


class Ship():
    def __init__(self, screen):
        """初始化飞船并设置其初始化位置"""
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        # get_rect()是一个处理矩形图像的方法，返回值包含矩形的居中属性（ center centerx centery ）
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每搜新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志
        self.moveing_right = False
        self.moveing_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 这里用两个if，不用elif是因为当玩家同时按下两个键时，即加一又减一，最后飞船不动，而不会优先判定向右
        if self.moveing_right:
            self.rect.centerx += 1
        if self.moveing_left:
            self.rect.centerx -= 1

    def blitme(self):
        """在指定位置绘制飞船"""
        # blit文档：https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        self.screen.blit(self.image, self.rect)
