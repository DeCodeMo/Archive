import pygame as pg
import sys, random, time
from settings import *
#from tools import *

# initialize game
pg.init() 
clock = pg.time.Clock() # init fps clock
pg.display.set_caption(TITLE)
game_font = pg.font.SysFont('Arial Bold',60) # for screen text
screen = pg.display.set_mode((SCREEN_W, SCREEN_H)) # define/init screen surface dims 
paddle_size = (SCREEN_W * 0.02, SCREEN_H * 0.10) # define scaled paddle size proportional to screen size (scaler/screen width = screen height)
ball_size = (SCREEN_W * 0.01953, SCREEN_H * 0.02604) # (scaler/screen width = screen height)

# background/court setup
# main display box
court_color = RGB('dodger blue')
scorebox_color = RGB('silver')
ibox_scale_percent = 10 #[%] scale the info box a given percentage of the screen
ibs = ((ibox_scale_percent)/100) # just a scalar calc for easy adjustment (i.e., 10% of screen is easy to visualize (not really needed))
infobox_size = (SCREEN_W, SCREEN_H*ibs) # dims (w, h)[px] for infobox
infobox = pg.Surface(infobox_size) # define infobox surface
info_rect = infobox.get_rect() # grab rectangle methods for infobox surface

# player 1 display box
p1box_size = ((info_rect.width/2)*0.95, info_rect.height*0.75)
p1box = pg.Surface(p1box_size)
p1box_rect = p1box.get_rect()
p1box_rect.center = (info_rect.right*0.25, info_rect.centery)

# cpu display box
cpubox_size = p1box_size
cpubox = pg.Surface(cpubox_size)
cpubox_rect = cpubox.get_rect()
cpubox_rect.center = (info_rect.right*0.75, info_rect.centery)

# center-line
line_color = court_color # define color for the center-line
line_start = (SCREEN_W / 2, 0) # line start position (x, y)
line_stop = (SCREEN_W / 2, SCREEN_H + info_rect.height) # line end position (x, y)

# player 1 setup
p1 = pg.image.load(PADDLE_IMAGE).convert_alpha() # load paddle png image
p1 = pg.transform.scale(p1, paddle_size) # rescale the player 1 paddle to new paddle size
p1_rect = p1.get_rect() # rect object of the paddle image
p1_rect.center = (p1_rect.w / 2, ((SCREEN_H + info_rect.height)/2)) # define the center position of the player 1 rect 

# cpu player setup
cpu = pg.image.load(PADDLE_IMAGE).convert_alpha() # load paddle png image
cpu = pg.transform.scale(cpu, paddle_size) # rescale the cpu paddle to new paddle size
cpu_rect = cpu.get_rect() # rect object of the paddle image
cpu_rect.center = (SCREEN_W - p1_rect.w / 2, (SCREEN_H  + info_rect.height)/2) # define the center position of the cpu rect (adjust left so it is on screen) 

# ball setup
ball = pg.image.load(BALL_IMAGE).convert_alpha() # load paddle png image
ball = pg.transform.scale(ball, ball_size) # rescale the cpu paddle to new paddle size
ball_rect = ball.get_rect() # rect object of the paddle image
ball_start = (SCREEN_W / 2, (SCREEN_H  + info_rect.height)/2) # define the center position of the ball rect (middle)
ball_speed = ball_dx, ball_dy = (BALL_SPEED, BALL_SPEED) # x and y velocity components of speed vector (not really using a vector here) 
ball_rect.center = ball_start # ball start/reset position

# flags
game_over = False # set game loop flag for clean exit
ball_in_play = False # set flag for ball reset
cpu_scored = False # flag to intialize score logic
player_scored = False # flag to initialize player logic
p1_won = False # declare player 1 the winner
cpu_won = False # declare cpu the winner
info_display = False # flag for button press to show debug info in caption
cpu_hit = False # bool for checking cpu paddle collision status
p1_hit = False # bool for checking player 1 paddle collision status

# initial conditions
p1_dy = 0 # inital state of position incrementer for player 1 y-coordinate
cpu_dy = 0 # inital state of position incrementer for cpu player y-coordinate
collision_count = 0 # count the number of consecutive paddle collisions 
player_score = 0 # count the number of times the player scores
cpu_score = 0  # count the number of times the cpu scores
max_score = 3 # set a score limit to determine a winner

# helpers
REV_BALL_SPEED = -BALL_SPEED

# player/cpu text rendering
# score text output
# score text output
score_text_color = RGB('tomato')
p1txt = 'Player: '
cputxt = 'CPU: '


# ball can go: (x, y), (x, -y), (-x, y), (-x, -y), (x, 0), (-x, 0)
bally_range = range(-1,1) # -1, 0, 1
ballx_range = (-1,1) # -1, 1
ball_dy *= random.choice(bally_range) # random initial y-direction or no y direction for ball start
ball_dx *= random.choice(ballx_range) # random initial x-direction for ball start 
p1_dir = None # a dummy variable, set initial value to None to show no movement of player 1 paddle initally
cpu_dir = None

timer = 0 # start time is 0
disp_timer = 0

ti = time.time() # timer starts (initial time) right before loop starts
# game loop
while not game_over:
	clock.tick(FPS)
	dt = time.time() - ti # the difference between the final and initial time gives us our delta time (change in time over one game-loop cycle)
	ti = time.time()
	timer += dt # increment the timer one unit of delta time each game-loop cycle
    # draw game objects
	screen.fill(pg.Color('black')) # fill screen background each frame to eliminate image smearing
	screen.blit(ball, ball_rect) # draw ball image
	screen.blit(p1, p1_rect) # draw player paddle image
	screen.blit(cpu, cpu_rect) # draw cpu paddle image
	screen.blit(infobox, (0,0)) # draw the infobox
	infobox.fill(court_color) # fill with color (using line_color for consistency)
	infobox.blit(p1box, p1box_rect) # draw the player 1 info display onto the info box surface
	infobox.blit(cpubox, cpubox_rect) # draw the cpu info display onto the info box surface
	p1box.fill(scorebox_color) # fill the score boxes with some color
	cpubox.fill(scorebox_color) # fill the score boxes with some color
	p1_text = game_font.render(f"{p1txt}{player_score}", False, score_text_color) # render text object 
	cpu_text = game_font.render(f"{cputxt}{cpu_score}", False, score_text_color) # render text object
	pr = p1_text.get_rect() # get the text rect object so we can center it easily on the score box rect
	cpr = cpu_text.get_rect() # get the text rect object so we can center it easily on the score box rect
	pr.center = (p1box_rect.centerx, p1box_rect.centery) # center of the text rect at the center of the score box
	cpr.center = (cpubox_rect.centerx, cpubox_rect.centery) # center of the text rect at the center of the score box
	screen.blit(p1_text, pr) # draw/update the text rect onto the score box sutrface
	screen.blit(cpu_text, cpr)# draw/update the text rect onto the score box sutrface

	# draw court center-line
	pg.draw.aaline(screen, court_color, line_start, line_stop) # center line

	for event in pg.event.get():
		match event.type: # match-case (python 3.10) is reportedly faster (test later, probably negligible)
			case pg.QUIT:
				game_over = True # exit the game loop
			case pg.KEYDOWN:
				if event.key == pg.K_ESCAPE: # close window and exit on escape key press
					pg.quit()
					sys.exit()
				if event.key == pg.K_w: # player 1 travels upward in -y dir with "w" key (reversed coordinate plane)
					p1_dy -= PADDLE_SPEED
					p1_dir = 'up    '
				if event.key == pg.K_s: # player 1 travels downward in y dir with "s" key (reversed coordinate plane)
					p1_dy += PADDLE_SPEED
					p1_dir = 'down '
				if event.key == pg.K_SPACE: # if spacebar is pressed, serve the ball in a random direction
					ball_in_play = True
					ball_xdir = None
					ball_ydir = None
				if event.key == pg.K_i: # if 'i' is pressed, start the display timer (10 seconds)
					info_display = True
					dspti = time.time()
			case pg.KEYUP: # sort of a debounce (so paddle immediately stops and does not skip around)
				if event.key == pg.K_w: # same as previous up increments y on keyup
					p1_dy += PADDLE_SPEED
					p1_dir = None
				if event.key == pg.K_s:
					p1_dy -= PADDLE_SPEED
					p1_dir = None

	# some direction strings for testing ball movement reaction to different collision tests
	if ball_in_play: # this is true when spacebar is pressed; false initially and again when a player scores
		if ball_dx > 0:  # ball is moving in x dir
			ball_xdir = 'right'
		if ball_dx < 0: # ball is moving in -x dir
			ball_xdir = 'left '
		if ball_dx == 0: # ball is not moving in x dir (stationary)
			ball_xdir = None
		if ball_dy > 0: # ball is moving in y dir (downward - remember it is reversed)
			ball_ydir = 'down '
		if ball_dy < 0: # ball is moving in -y dir (upward - remember it is reversed)
			ball_ydir = 'up   '
	else: # just to be thorough
		ball_xdir = None
		ball_ydir = None

    # movement/animations
	p1_rect.y += p1_dy # increment player 1 y-coordinate the value of p1_dy (determined by keypress)
	
	if ball_in_play: # event becomes true and ball moves when spacebar is pressed
		ball_rect.y += ball_dy  # increment ball by value of ball_dy on the y-axis 
		ball_rect.x += ball_dx  # increment ball by value of ball_dx on the x-axis

	# ball boundaries/top...(0, 0) = (x, y) = top left window corner
	if ball_rect.y <= info_rect.bottom:  # changed to bottom of infobox rect
		ball_rect.y = info_rect.bottom
		ball_dy *= -1 # reflect back in negative y-direction

	# ball boundaries/bottom
	if ball_rect.y >= SCREEN_H - ball_rect.height: 
		ball_rect.y = SCREEN_H - ball_rect.height
		ball_dy *= -1 # reflect back in positive y-direction

	# ball boundaries/left - cpu scored
	if ball_rect.x <= 0:
		cpu_scored = True
		if cpu_score == max_score:
			cpu_won = True

	# ball boundaries/right - player scored
	if ball_rect.x >= SCREEN_W:
		player_scored = True
		if player_score == max_score:
			p1_won = True

	# paddle boundaries (only in y-dir)
	# player 1
	if p1_rect.top <= info_rect.bottom:
		p1_rect.top = info_rect.bottom
	if p1_rect.bottom >= SCREEN_H:
		p1_rect.bottom = SCREEN_H

	# cpu movement
	# boundaries
	if cpu_rect.top <= info_rect.bottom:
		cpu_rect.top = info_rect.bottom
	if cpu_rect.bottom >= SCREEN_H:
		cpu_rect.bottom = SCREEN_H

	# autoplay  
    # #TODO this could be improved  
	if cpu_rect.top < ball_rect.centery:
		cpu_rect.y += CPU_SPEED
	if cpu_rect.bottom > ball_rect.centery:
		cpu_rect.y -= CPU_SPEED




	# handle paddle collisions and account for collisions with top of paddles
	if ball_rect.colliderect(cpu_rect) and ball_dx > 0: # ball moving right
		cpu_hit = True
		BALL_SPEED+=0.1
		ball_xdir = None
		ball_ydir = None
		collision_count += 1
		if ball_ydir == None: # if there is no y-dir movement, set speed in a random y-direction (if not, it will stay staight)
			ball_dy = random.choice((-BALL_SPEED, BALL_SPEED, 0))
		if abs(ball_rect.right - cpu_rect.left) < cpu_rect.width: # fix top collision
			ball_dx *= -1 # reflect in opposite y-dir
		elif abs(ball_rect.bottom - cpu_rect.top) < cpu_rect.width and ball_dy > 0:
			ball_dy *= -1 # reflect in opposite y-dir
		elif abs(ball_rect.top - cpu_rect.bottom) < cpu_rect.width and ball_dy < 0:
			ball_dy *= -1 # reflect in opposite y-dir

	if ball_rect.colliderect(p1_rect) and ball_dx < 0: # ball moving left
		BALL_SPEED+=0.1
		p1_hit = True
		ball_xdir = None
		ball_ydir = None
		collision_count += 1
		if ball_ydir == None: # if there is no y-dir movement, set speed in a random y-direction (if not, it will stay staight)
			ball_dy = random.choice((-BALL_SPEED, BALL_SPEED, 0))
		if abs(ball_rect.left - p1_rect.right) < p1_rect.width: # fix top collision
			ball_dx *= -1
		elif abs(ball_rect.bottom - p1_rect.top) < p1_rect.width:
			ball_dy *= -1
		elif abs(ball_rect.top - p1_rect.bottom) < p1_rect.width:
			ball_dy *= -1

	# some improved mechanics
	# TODO finish this later

	# score logic
	while cpu_scored:
		ball_xdir = None
		ball_ydir = None
		collision_count = 0
		cpu_score += 1
		cpu_text = game_font.render(f"{cputxt}{cpu_score}", False, score_text_color)
		ball_rect.center = ball_start
		ball_dx, ball_dy = (5, 5) # reset the values
		ball_dy *= random.choice(bally_range) # random inital y-direction or no y direction for ball start 
		ball_dx *= random.choice(ballx_range) # random inital x-direction for ball start
		cpu_scored = False 

	while player_scored:
		ball_xdir = None
		ball_ydir = None
		collision_count = 0
		player_score += 1
		p1_text = game_font.render(f"{p1txt}{player_score}", False, score_text_color)
		ball_rect.center = ball_start
		ball_dx, ball_dy = (5, 5) # reset the values
		ball_dy *= random.choice(bally_range) # # random inital y-direction or no y direction for ball start 
		ball_dx *= random.choice(ballx_range) # random inital x-direction for ball start 
		player_scored = False



	if p1_won or cpu_won:
		player_score, cpu_score = 0, 0
		p1_won, cpu_won = False, False

	fps = (" FPS: [{}]").format(round(clock.get_fps(),0))
	hits = (" Hits: [{}]").format(collision_count)
	p1score = (" Player1 Score: [{}]").format(player_score)
	cpuscore = (" CPU Score: [{}]").format(cpu_score)
	pdir = (" Player dir: [{}]").format(p1_dir)
	bdir = (" Ball dir: [{},{}]").format(ball_xdir, ball_ydir)
	d_t = (" Game Time: [{} sec] ").format(round(timer, 1))

	#some debugging output (turns on by pressing 'i' key)
	if info_display:
		dspt = time.time() - dspti 
		dspti = time.time()
		disp_timer += dspt 
		pg.display.set_caption(TITLE+str(fps)+str(hits)+str(p1score)+str(cpuscore)+str(pdir)+str(bdir)+str(d_t))
		disp_timer += dt
		if disp_timer > 1000: # set high temporarily
			disp_timer = 0
			pg.display.set_caption(TITLE)
			info_display = False

	pg.display.update() # update the pygame display last, [!] add framerate independence for consistency
	#clock.tick(FPS) # count a tick for each frame at the FPS rate defined in settings.py (usually 60)


pg.quit() # quit pygame
sys.exit() # clean exit