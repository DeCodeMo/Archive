
# Draw some sprites 

import pygame as pg
import sys

WIDTH = 360
HEIGHT = 480
FPS = 30
TITLE = "Game Template"

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT))
all_sprites = pg.sprite.Group()
clock = pg.time.Clock()

def setup_game():
    # initialize window
    pg.init()
    pg.mixer.init()
    pg.display.set_caption(TITLE)

def run_event_loop():
    # Game loop
    game_over = False
    while not game_over:
        clock.tick(FPS)
        # events
        for event in pg.event.get():
            # check for quit
            if event.type == pg.QUIT:
                game_over = True
            # define player controls
            if event.type == pg.KEYDOWN:
                # escape key closes game window
                if event.key == pg.K_ESCAPE:
                    quit_game()

def draw_objects():
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

def update_game():
    # Update
    all_sprites.update()

    ####################
    draw_objects()
    ####################

    # flip the display
    pg.display.flip()

def quit_game():
    pg.quit()
    sys.exit()

def run_game():
    setup_game()
    run_event_loop()
    update_game()


if __name__ == '__main__':
    run_game()
    quit_game()








