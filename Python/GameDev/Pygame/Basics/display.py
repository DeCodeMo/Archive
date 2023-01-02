
# Basic display screen to get started with Pygame

import pygame as pg
import sys

pg.init()
fps_clock = pg.time.Clock()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Pygame Template #1")

all_sprites = pg.sprite.Group()

game_over = False

while not game_over:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()


    pg.display.set_caption((f"Pygame Template #1 [Current FPS: {int(fps_clock.get_fps())}]"))
    pg.display.flip()
    fps_clock.tick(30)
    

pg.quit()
sys.exit()