import pygame as pg
import numpy as np
import os

RGB = pg.Color # just for convenience

''' <<<<<<<<<<<<<<<<< GAME SETTINGS / CONSTANTS >>>>>>>>>>>>>>>''' 
#-------------------- window setup -------------------------
SCREEN_W = 1280 # screen height 
SCREEN_H = 960
SCREEN_SIZE = [SCREEN_W, SCREEN_H]
SCREEN_CENTER = [wh//2 for wh in SCREEN_SIZE]
#-------------------- general settings ---------------------
TITLE = "Cosmic Pong!"
FPS = 70
BACKGROUND_COLOR = RGB('black')
BOUNDARY_COLOR = RGB('gray')
MUSIC_VOLUME = 8
SOUND_EFFECTS_VOLUME = 3
#------------------- player settings ------------------------
PADDLE_SPEED = 9
CPU_SPEED = 5
BALL_SPEED = 7
MAX_SCORE = 5
PADDLE_COLOR = 'gray'
BALL_COLOR = 'white'
#--------------------- key bindings -------------------------
EXIT_WINDOW = pg.K_ESCAPE
PLAYER1_CONTROLS = {'up':pg.K_w,'down':pg.K_s}
PLAYER2_CONTROLS = {'up':pg.K_UP,'down':pg.K_DOWN}
#------------------ asset file paths ------------------------- 
ASSET_DIR = os.path.join(os.path.dirname(__file__), 'assets')
ASSETS = {
    'images': os.path.join(ASSET_DIR, 'images'),
    'sound': os.path.join(ASSET_DIR, 'sound'),
    'music': os.path.join(ASSET_DIR, 'music')
}
# images
PADDLE_IMAGE = os.path.join(ASSETS['images'], 'paddle.png')
BALL_IMAGE = os.path.join(ASSETS['images'], 'ball.png')
# sound effects
PADDLE_STRIKE_SOUND = os.path.join(ASSETS['sound'], 'pad_strike.mp3')
SCORE_SOUND = os.path.join(ASSETS['sound'], 'score.mp3')
# music
BACKGROUNG_MUSIC = os.path.join(ASSETS['music'], 'bkg_music1.mp3')