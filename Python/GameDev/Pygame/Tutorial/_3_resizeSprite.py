
import pygame

# ## Resize a Sprite

# init pygame
pygame.init()

# set screen size (pixels)
WIDTH = 1000
HEIGHT = 800
SCREEN_SIZE = [WIDTH, HEIGHT]
# sprite size (pixels)
SPRITE1_SIZE = [32,32]
#set title
TITLE = "Hello Sprite"

# fill screen color (RGB)
BLACK = (0,0,0)

# set a game state flag
game_over = False

# define image file
sprite1 = pygame.image.load('rocket.png')

# transform rocket to 64,64
sprite1 = pygame.transform.scale(sprite1, (64,64))

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
            
    # blit method for drawing sprite onto display, must give it a position ((0,0) --> origin)
    # the method maps the center of the sprite to the center of the screen
    screen.blit(sprite1, ((SCREEN_SIZE[0]-SPRITE1_SIZE[0])/2, (SCREEN_SIZE[1]-SPRITE1_SIZE[1])/2))
    # must refresh in order to update the screen
    pygame.display.update()
            
# quit method outside of loop
pygame.quit()