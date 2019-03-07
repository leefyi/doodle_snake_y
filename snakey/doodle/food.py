#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-03-07 23:05
# @Author  : lifangyi
# @File    : food.py
# @Software: PyCharm


# 食物类
# 初始化食物位置
# 随机生成食物

import pygame
import numpy as np
from constant import BOARDHEIGHT, BOARDWIDTH


class Food(object):
    def __init__(self):
        self.item=(4,5)

    # 画出食物
    def _draw(self,screen,i,j):
        color=255,0,255
        radius=10
        width=10

        position=10+20*i,10+20*j
        pygame.draw.circle(screen,color,position,radius,width)

    # 随机生成食物
    def gen_food(self,screen,eaten,snake):
        if eaten:
            self.item=np.random.randint(1,BOARDWIDTH-2),np.random.randint(1,BOARDHEIGHT-2)
            # 如果新生成的食物 在 蛇内部，则重新生成
            while self.item in snake.item:
                self.item = np.random.randint(1, BOARDWIDTH - 2), np.random.randint(1, BOARDHEIGHT - 2)
        self._draw(screen,self.item[0],self.item[1])