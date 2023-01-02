
# Example Game class implementation

import pygame as pg
import sys

WIDTH = 800
HEIGHT = 600
FPS = 30
TITLE = "Game Template #3"
BKG_COLOR = 'black'

class Game:
    def __init__(self):
        pg.init()
        self.screen_size = [WIDTH, HEIGHT]
        self.RGB = pg.Color
        self.screen = pg.display.set_mode(self.screen_size)
        self.screen.fill(self.RGB(BKG_COLOR))

    def setup(self):
        # initialize window
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()

    def events(self):
        # Game loop
        game_over = False
        while not game_over:
            self.clock.tick(FPS)
            # events
            for event in pg.event.get():
                # check for quit
                if event.type == pg.QUIT:
                    game_over = True
                # define player controls
                if event.type == pg.KEYDOWN:
                    # escape key closes game window
                    if event.key == pg.K_ESCAPE:
                        self.quit_game()
            self.update()

    def draw(self):
        # Draw 
        pass

    def update(self):
        # Update
        self.screen.fill(self.RGB(BKG_COLOR))
        ####################
        self.draw()
        ####################
        # flip the display
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def run(self):
        self.setup()
        self.events()
        self.quit()

game = Game()
if __name__ == '__main__':
        game.run()