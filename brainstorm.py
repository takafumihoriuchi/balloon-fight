# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *  # constants such as QUIT
import sys

SCREEN_W = 1200
SCREEN_H = 800
SCREEN_SIZE = (SCREEN_W, SCREEN_H)

pygame.init()
# may create only one screen with set_mode()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("balloonfight")

x = 640
y = 420
vx = 20
vy = 20
img = pygame.image.load("./images/img_fly.gif").convert_alpha()
img_rect = img.get_rect()
img_rect.center = (x, y)

img_enemy = pygame.image.load("./images/mario.gif").convert_alpha()

# game loop
while True:
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] and (x > 0):
        img_rect.move_ip(-vx, 0)
        x -= vx
    if pressed_keys[K_RIGHT] and (x < SCREEN_W):
        img_rect.move_ip(vx, 0)
        x += vx
    if pressed_keys[K_UP] and (y > 0):
        img_rect.move_ip(0, -vy)
        y -= vy
    if pressed_keys[K_DOWN] and (y < SCREEN_H):
        img_rect.move_ip(0, vy)
        y += vy

    screen.fill((0,0,0))  # screen color
    
    screen.blit(img_enemy, (SCREEN_W/2, SCREEN_H/2))
    screen.blit(img, img_rect)
    
    pygame.display.update()  # update screen
    # events
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()  # when pressed red 'x' on the corner of the window
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()


"""
references


~structure of game-loops~

while True:
    update game objects
    render game objects
    update screen
    process events
"""