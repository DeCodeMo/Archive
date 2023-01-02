import pygame

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
BLACK = (255,0,0)

# set a game state flag
game_over = False

############################### Main code ################################# 

screen = pygame.display.set_mode(SCREEN_SIZE) # display the scrren 

pygame.display.set_caption(TITLE) # display the title

screen.fill(BLACK) # fill the screen with color

# begin game loop
while not game_over:
    # event handler
    for event in pygame.event.get():
        # check for quit event (i.e. closing pygame box)
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill(BLACK)
    pygame.display.flip()
# quit method outside of loop
pygame.quit()