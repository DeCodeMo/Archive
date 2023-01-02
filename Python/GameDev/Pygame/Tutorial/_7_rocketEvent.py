
# ## Add an event to put rocket at top left if space bar is pressed

import pygame as pg
from pygame.locals import *

pg.init()

WIDTH = 1000
HEIGHT = 800
SCREEN_SIZE = [WIDTH, HEIGHT]

BLACK = (0,0,0)

screen = screen = pg.display.set_mode(SCREEN_SIZE)

rocket_img = pg.image.load('fowler_sprite.png')
rocket_img = pg.transform.scale(rocket_img, (64,64))

rocket_height = rocket_img.get_height()
rocket_width = rocket_img.get_width()

pg.display.set_caption("Moving a Sprite")

screen.fill(BLACK)

game_over = False

x,y = (0,0)

clock = pg.time.Clock() # clock method

while not game_over:
    dt = clock.tick(60) # set to 60 frames per second
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
    pressed = pg.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt # multiply the change in time by the movement scaler
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    ################################ New Event ###################################
    if pressed[K_SPACE]:
        x,y = (0,0)
    ##############################################################################
    screen.fill(BLACK) 
    screen.blit(rocket_img, (x,y))
    pg.display.update()
    
pg.quit()  