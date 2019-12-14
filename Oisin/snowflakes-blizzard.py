import random, sys, time, math, pygame
from pygame.locals import *

from pygame import gfxdraw


FPS = 60 # frames per second to update the screen
WINWIDTH = 1090 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
MAXSPEED = 5
MOVERATE = 1
flakespeed = 1
NBLINES = 1
NBSNOW = 2000

MAXWIND = 10

black = (0,0,0,255)
white = (255,255,255,255)

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('boss')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

   
    while True:
        runGame()
   
def terminate():
    pygame.quit()
    sys.exit()
   
def runGame():
    global NBSNOW,flakespeed
    random.seed(time.time())
   
    player = {
                 'x': HALF_WINWIDTH,
                 'y': HALF_WINHEIGHT,
                 'color' : (255,0,0),
                 }

    flakes = []
    for n in range(NBSNOW):
      color = random.randint(192, 255)
      flakes.append( {
                 'x': random.randint(0,WINWIDTH-1),
                 'y': random.randint(-WINHEIGHT,0),
                 'color' : (color,color,color),
                 } )

    bottom_line = [ WINHEIGHT ] * WINWIDTH                 
                  
    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False

     

    wind = random.randint(-MAXWIND, MAXWIND)

    while True: # main game loop
        if moveUp : flakespeed = flakespeed-1 
	if moveDown : flakespeed = flakespeed+1
        
        # Handle wind
        if  moveLeft : wind = wind-1
	if moveRight : wind = wind+1 
        if wind < -MAXWIND:
                wind = -MAXWIND
        if wind > MAXWIND:
                wind = MAXWIND
        
	if moveRight : wind = wind+1 
        if wind < -MAXWIND:
                wind = -MAXWIND
        if wind > MAXWIND:
                wind = MAXWIND
        
        for n in range(NBSNOW):
            flake = flakes[n]

	    # Get flake new position
	    new_x = flake['x'] + wind
	    new_y = flake['y'] + random.randint(0,MAXSPEED)+(flakespeed)

	    # Make sure the flake stays on screen
            if new_x < 0:
                new_x += WINWIDTH
            if new_x >= WINWIDTH:
                new_x -= WINWIDTH

	    # If the color is not black, we move the flake
	    if new_y < bottom_line[ new_x ]:

               # Clear flake
               gfxdraw.pixel(DISPLAYSURF, flake['x'], flake['y'], black)

               flake['x'] = new_x
               flake['y'] = new_y
                
	       # Draw flake
               gfxdraw.pixel(DISPLAYSURF, flake['x'], flake['y'], flake['color'])

	    else:
               bottom_line[ flake['x'] ] = flake['y']

	       # Otherwise, we move the flake back to the top
               flake['x'] = random.randint(0,WINWIDTH-1)
               flake['y'] = random.randint(-WINHEIGHT//2,0)

		

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
				
            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    moveDown = False
                    moveUp = True
                elif event.key in (K_DOWN, K_s):
                    moveUp = False
                    moveDown = True
                elif event.key in (K_LEFT, K_a):
                    moveRight = False
                    moveLeft = True
                elif event.key in (K_RIGHT, K_d):
                    moveLeft = False  
                    moveRight = True
		elif event.key == K_SPACE:
                    pygame.draw.rect(DISPLAYSURF, black, (0,0,WINWIDTH,WINHEIGHT)) 
		    bottom_line = [ WINHEIGHT ] * WINWIDTH 
            elif event.type == KEYUP:
 
                if event.key in (K_LEFT, K_a):
                    moveLeft = False
                elif event.key in (K_RIGHT, K_d):
                    moveRight = False
                elif event.key in (K_UP, K_w):
                    moveUp = False
                elif event.key in (K_DOWN, K_s):
                    moveDown = False

                elif event.key == K_ESCAPE:
                    terminate()

        #if not gameOverMode:
            # actually move the player
        if moveLeft:
                player['x'] -= MOVERATE
        if moveRight:
                player['x'] += MOVERATE
        if moveUp:
                player['y'] -= MOVERATE
        if moveDown:
                player['y'] += MOVERATE
            
                     
        pygame.display.update()
        FPSCLOCK.tick(FPS)
     
if __name__ == '__main__':
    main()
