# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *  # 定数を格納（QUITなど）
import sys
 
SCREEN_SIZE = (640, 480)

pygame.init()
# set_mode()での画面の作成は一つのみ
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("balloonfight")

characterImg = pygame.image.load("animados093.gif").convert_alpha()

# game loop
while True:
    screen.fill((220,220,220))  # 画面を青色で塗りつぶす
    screen.blit(characterImg, (320,240))
    pygame.display.update()  # 画面を更新
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # when pressed red 'x' on the corner of the window
            sys.exit()

"""
一般的なゲームループの構造
    while True:
        ゲームオブジェクトの更新
        ゲームオブジェクトのレンダリング（描画）
        画面の更新
        イベント処理
"""