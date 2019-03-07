#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-03-07 23:05
# @Author  : lifangyi
# @File    : game.py
# @Software: PyCharm

import pygame
import time
import constant
from pygame.locals import *
from food import Food
from snake import Snake


# 游戏处理与运行时类

# 初始页面


def init_board(screen):
    board_width = constant.BOARDWIDTH
    board_height = constant.BOARDHEIGHT
    # 边框颜色，一种浅亮蓝色
    # #0AFFFF
    color = 10, 255, 255
    width = 0

    for i in range(board_width):
        # 下边框
        pos = i * 20, 0, 20, 20
        pygame.draw.rect(screen, color, pos, width)
        # 上边框
        pos = i * 20, (board_height - 1) * 20, 20, 20
        pygame.draw.rect(screen, color, pos, width)

    for j in range(board_height - 1):
        # 左边框
        pos = 0, 20 + j * 20, 20, 20
        pygame.draw.rect(screen, color, pos, width)
        # 右边框
        pos = (board_width - 1) * 20, 20 + j * 20, 20, 20
        pygame.draw.rect(screen, color, pos, width)

# 游戏失败处理


def game_over(snake):
    board_x, board_y = snake.get_head()
    flag = 0
    old_l = len(snake.item)
    new_l = len(set(snake.item))

    # 蛇头碰到蛇身
    # gg
    if new_l < old_l:
        flag = 1

    if board_x == 0 or board_x == constant.BOARDWIDTH - 1:
        flag = 1
    if board_y == 0 or board_y == constant.BOARDHEIGHT - 1:
        flag = 1

    if flag:
        return True
    else:
        return False

# 打印字符


def print_text(screen, font, x, y, text, color=(255, 0, 0)):
    imgText = font.render(text, True, color)
    # 将文本 text 以color代表的颜色 画在(x,y)位置
    screen.blit(imgText, (x, y))

# 按键
# 这些常量无法正常显示，但实际可以访问到，可以正常运行


def press(keys, snake):
    global score
    # 下移
    if keys[K_w] or keys[K_UP]:
        snake.towards(0, -1)
    # 上移
    elif keys[K_s] or keys[K_DOWN]:
        snake.towards(0, 1)
    # 左移
    elif keys[K_a] or keys[K_LEFT]:
        snake.towards(-1, 0)
    # 右移
    elif keys[K_d] or keys[K_RIGHT]:
        snake.towards(1, 0)
    # 重置游戏
    elif keys[K_r]:
        score = 0
        lancher()
    # 退出游戏
    elif keys[K_ESCAPE]:
        exit()

# 游戏初始化


def game_init():
    pygame.init()
    screen = pygame.display.set_mode(
        (constant.BOARDWIDTH * 20, constant.BOARDHEIGHT * 20))
    pygame.display.set_caption('骚毅的贪吃蛇')
    return screen

# 游戏主进程


def game(screen):
    snake = Snake()
    food = Food()
    # 设置中文字体和大小
    font = pygame.font.SysFont('SimHei', 20)
    is_fail = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        # 填充屏幕的颜色
        # 一种深蓝色 #000064
        screen.fill((0, 0, 100))
        init_board(screen=screen)
        # 获得用户按键命令
        keys = pygame.key.get_pressed()
        press(keys, snake)
        # 游戏失败打印提示
        if is_fail:
            font2 = pygame.font.Font(None, 40)
            print_text(screen, font, 0, 0, text)
            print_text(screen, font2, 400, 200, "GAME OVER")
        # 游戏主进程
        if not is_fail:
            eaten = snake.eat(food)
            text = u"score: {}".format(Snake.score)
            print_text(screen, font, 0, 0, text)
            food.gen_food(screen, eaten, snake)
            snake.move(eaten)
            is_fail = game_over(snake=snake)
            snake.draw(screen)
        # 游戏刷新
        pygame.display.update()
        time.sleep(0.1)

# 启动程序


def lancher():
    screen = game_init()
    game(screen)


# run

if __name__ == '__main__':
    lancher()
