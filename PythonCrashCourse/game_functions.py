# -*- coding: utf-8 -*-
# @Time : 2019-06-16 21:16
# @Author : HuJiangong
# @File : game_functions.py
# @Version : Python 3.6.5
# @Software: PyCharm

import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = True
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moveing_right = False
    elif event.key == pygame.K_LEFT:
        ship.moveing_left = False


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # pygame.sprite 用法
    aliens.draw(screen)

    # 在飞船和外星人后面重新绘制所有子弹:
    # bullets.sprites() 返回一种列表，其包含编组bullets中的所有精灵
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_buttet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞，只要和第一个飞船发生碰撞，groupcollide()返回不为空即满足条件
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果没有达成子弹上限，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if (len(bullets) < ai_settings.bullet_allowed):
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, number_rows):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_rows

    aliens.add(alien)


def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for rows in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, rows)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_buttet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """相应子弹和外星人的碰撞"""
    # 就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 如果剩余的外星人为空了
    if len(aliens) == 0:
        # 删除先由的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        creat_fleet(ai_settings, screen, ship, aliens)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """如果玩家点击play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:

        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
