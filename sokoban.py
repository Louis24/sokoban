#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2023/3/9 10:41
#  @Author  : Louis Li
#  @Email   : vortex750@hotmail.com

import sys
import numpy as np
import pygame

# 初始化 Pygame
pygame.init()

# 游戏窗口大小
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 创建游戏窗口
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('推箱子')

# 加载图片
player_img = pygame.image.load('player.png')
floor_img = pygame.image.load('floor.png')
wall_img = pygame.image.load('wall.png')
box_img = pygame.image.load('box.png')
goal_img = pygame.image.load('target.png')

# 设置图像大小
player_img = pygame.transform.scale(player_img, (50, 50))
wall_img = pygame.transform.scale(wall_img, (50, 50))
box_img = pygame.transform.scale(box_img, (50, 50))
goal_img = pygame.transform.scale(goal_img, (50, 50))

# 游戏地图，0表示空地，1表示墙，2表示箱子，3表示目标点
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# 获取地图上指定位置的值
def get_map_value(x, y):
    if x < 0 or x >= len(map_data) or y < 0 or y >= len(map_data[0]):
        return None
    return map_data[x][y]


# 绘制地图
def draw_map():
    for x in range(len(map_data)):
        for y in range(len(map_data[x])):
            value = map_data[x][y]
            if value == 0:
                window.blit(floor_img, (x * 50, y * 50))
            elif value == 1:
                window.blit(wall_img, (x * 50, y * 50))
            elif value == 2:
                window.blit(box_img, (x * 50, y * 50))
            elif value == 3:
                window.blit(goal_img, (x * 50, y * 50))


def is_win():
    for x in range(len(map_data)):
        for y in range(len(map_data[x])):
            if map_data[x][y] == 3:
                return False
    return True


def main():
    # 玩家初始位置
    player_x = 1
    player_y = 1

    # 游戏循环标志位
    running = True

    # 游戏主循环
    while running:


        # 处理事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         running = False
        #     # elif event.type == pygame.KEYDOWN:

            # 移动玩家 + 不能撞墙 + 不能推2箱

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # while event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        if keys[pygame.K_UP]:
            if get_map_value(player_x, player_y - 1) == 0 or get_map_value(player_x, player_y - 1) == 3:
                player_y -= 1
            elif get_map_value(player_x, player_y - 1) == 2 and get_map_value(player_x, player_y - 2) != 1:
                player_y -= 1
                map_data[player_x][player_y] = 0
                map_data[player_x][player_y - 1] = 2

        # while event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        if keys[pygame.K_DOWN]:
            if get_map_value(player_x, player_y + 1) == 0 or get_map_value(player_x, player_y + 1) == 3:
                player_y += 1
            elif get_map_value(player_x, player_y + 1) == 2 and get_map_value(player_x, player_y + 2) != 1:
                player_y += 1
                map_data[player_x][player_y] = 0
                map_data[player_x][player_y + 1] = 2

        # while event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:

        if keys[pygame.K_LEFT]:
            if get_map_value(player_x - 1, player_y) == 0 or get_map_value(player_x - 1, player_y) == 3:
                player_x -= 1
            elif get_map_value(player_x - 1, player_y) == 2 and get_map_value(player_x - 2, player_y) != 1:
                player_x -= 1
                map_data[player_x][player_y] = 0
                map_data[player_x - 1][player_y] = 2

        # while event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        if keys[pygame.K_RIGHT]:
            if get_map_value(player_x + 1, player_y) == 0 or get_map_value(player_x + 1, player_y) == 3:
                player_x += 1
            elif get_map_value(player_x + 1, player_y) == 2 and get_map_value(player_x + 2, player_y) != 1:
                player_x += 1
                map_data[player_x][player_y] = 0
                map_data[player_x + 1][player_y] = 2

        # print(np.array(map_data))

        # 绘制背景
        window.fill(BLACK)

        # 绘制地图
        draw_map()

        # 绘制玩家
        window.blit(player_img, (player_x * 50, player_y * 50))

        # 判断是否胜利
        if is_win():
            font = pygame.font.SysFont(None, 48)
            text = font.render('YOU WIN!', True, GREEN)
            window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

        # 更新屏幕
        pygame.display.update()
        pygame.time.Clock().tick(25) # 不加这句是cpu频率速度快

    # 退出 Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
