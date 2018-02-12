# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *  # constants such as QUIT
import sys

SCREEN_SIZE = (1200, 800)

pygame.init()
# may create only one screen with set_mode()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("balloonfight")

img = pygame.image.load("./images/img_fly.gif").convert_alpha()
img_rect = img.get_rect()
img_rect.center = (640, 420)

vx = vy = 20

# game loop
while True:
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] && :
        img_rect.move_ip(-vx, 0)
    if pressed_keys[K_RIGHT]:
        img_rect.move_ip(vx, 0)
    if pressed_keys[K_UP]:
        img_rect.move_ip(0, -vy)
    if pressed_keys[K_DOWN]:
        img_rect.move_ip(0, vy)

    screen.fill((0,0,0))  # screen color
    
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