# # Monitoring Mouse Motion

import pygame as pg
from pygame.locals import *

pg.init()

WIDTH = 1000
HEIGHT = 800
SCREEN_SIZE = [WIDTH, HEIGHT]

BLACK = (0,0,0)

screen = pg.display.set_mode(SCREEN_SIZE)

rocket_img = pg.image.load('fowler_sprite.png')
rocket_img = pg.transform.scale(rocket_img, (256,256))

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
        ############# Mouse motion ###################
        elif event.type == pg.MOUSEMOTION:
            x,y = event.pos
            # center the control
            x = rocket_width/2
            y = rocket_height/2
        ##############################################    
    pressed = pg.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt # multiply the change in time by the movement scaler
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x,y = (0,0)
    if x > (WIDTH - rocket_width):
        x = WIDTH - rocket_width
    if y > (HEIGHT - rocket_height):
        y = HEIGHT - rocket_height
    if x < 0:
        x = 0
    if y < 0:
        y = 0 
    screen.fill(BLACK) 
    screen.blit(rocket_img, (x,y))
    pg.display.update()
pg.quit() 
