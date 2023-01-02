# ## Render some simple text

import pygame
from pygame.locals import *
from _A_colorDict import *

# Init screen
pygame.init()

screen = pygame.display.set_mode((800, 800*0.8))

pygame.display.set_caption('Basic Pygame program')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(RGB('white'))

# Display some text
font = pygame.font.Font(None, int(800*0.1))
text = font.render("Welcome to Pygame", 1, RGB('black'))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

# Blit everything to the screen
screen.blit(background, (0, 0))

# update
pygame.display.flip()
    
game_over = False  

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
    screen.blit(background, (0, 0))
    pygame.display.flip()
print(f"Text Center Position (x, y) = ({textpos.x},{textpos.y})") 
print(f"Text Size in Pixels (Width, Height) = {text.get_size()}")
pygame.quit()
