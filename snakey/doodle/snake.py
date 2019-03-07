#!/usr/local/bin python
# coding=utf-8
# @Time    : 2019-03-07 23:05
# @Author  : lifangyi
# @File    : snakey.py
# @Software: PyCharm


# Snake类，
# 用于初始化 贪吃蛇
# 并定义移动，吃等动作
# 变换形态，渲染

import pygame

# 全局变量，初始化分数

class Snake(object):

    score=0
    def __init__(self):
        self.item=[(3,25),(2,25),(1,25),(1,24),]
        # 初始移动方向
        self.x=0
        self.y=-1

    def move(self,eaten):
        # 如果没吃到食物
        # 向toward方向移动了，移动方向加一格子，蛇尾减一格子
        if not eaten:
            self.item.pop()

        head=(self.item[0][0]+self.x,self.item[0][1]+self.y)

        # 将新的蛇头坐标插入在item最前面
        self.item.insert(0,head)

    def eat(self,food):
        global score
        # 如果吃到了食物,+10分
        snake_x,snake_y=self.item[0]
        food_x,food_y=food.item

        # 比较蛇头坐标与食物坐标
        if (food_x==snake_x) and (food_y==snake_y):
            Snake.score+=10
            return 1
        else:
            return 0

    def towards(self,x,y):
        # 移动方向
        if self.x * x >=0 and self.y * y >=0:
            self.x=x
            self.y=y

    def get_head(self):
        # return tuple
        return self.item[0]

    def draw(self,screen):

        # 画出蛇
        radius=15
        width=15

        # 蛇头
        color=255,0,0
        position=10+20* self.item[0][0],10+20 * self.item[0][1]
        pygame.draw.circle(screen,color,position,radius,width)

        # 蛇身
        radius=10
        width=10
        for i, j in self.item[1:]:
            position=10+20*i, 10+20*j
            pygame.draw.circle(screen,color,position,radius,width)