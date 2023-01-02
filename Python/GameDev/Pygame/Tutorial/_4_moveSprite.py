# ## Move a Sprite with a Keyboard

import pygame as pg
from pygame.locals import *
import numpy as np

pg.init()

WIDTH = 1000
HEIGHT = 800
SCREEN_SIZE = [WIDTH, HEIGHT]

BLACK = (0,0,0)

screen = screen = pg.display.set_mode(SCREEN_SIZE)

rocket_img = pg.image.load('rocket.png')
rocket_img = pg.transform.scale(rocket_img, (256,256))

rocket_height = rocket_img.get_height()
rocket_width = rocket_img.get_width()

pg.display.set_caption("Moving a Sprite")

screen.fill(BLACK)

game_over = False

x,y = (0,0)

while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
    pressed = pg.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5
    if pressed[K_DOWN]:
        y += 0.5
    if pressed[K_LEFT]:
        x -= 0.5
    if pressed[K_RIGHT]:
        x += 0.5
    screen.blit(rocket_img, (x,y))
    pg.display.update()
    
pg.quit()      
