# ## Render arc and polygon


import pygame
from math import pi
from _A_colorDict import *

########################### Setup ##############################

# init pygame
pygame.init()

# set screen size
WIDTH = 1000
HEIGHT = 800
SCREEN_SIZE = [WIDTH, HEIGHT]

#set title
TITLE = "Hello Pygame"

# fill screen color (RGB)
BACKGROUND = RGB('white')

# set a game state flag
game_over = False

############################### Main code ################################# 

screen = pygame.display.set_mode(SCREEN_SIZE) # display the scrren 

pygame.display.set_caption(TITLE) # display the title

screen.fill(BACKGROUND) # fill the screen with color

# begin game loop
while not game_over:
    # event handler
    for event in pygame.event.get():
        # check for quit event (i.e. closing pygame box)
        if event.type == pygame.QUIT:
            game_over = True
    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    pygame.draw.arc(screen, RGB('black'),[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, RGB('green'),[210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, RGB('blue'), [210, 75, 150, 125], pi,3*pi/2, 2)
    pygame.draw.arc(screen, RGB('red'), [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    pygame.draw.polygon(screen, RGB('purple'), [[WIDTH*0.5-20, HEIGHT*0.5+20], [WIDTH*0.5-10, HEIGHT*0.5+10], [200, 200]], 5)
    pygame.display.flip()
            
# quit method outside of loop
pygame.quit()