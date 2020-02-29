import random, sys, time, math, pygame
from pygame.locals import *

from pygame import gfxdraw


FPS = 100 # frames per second to update the screen
WINWIDTH = 1090 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
MAXSPEED = 1
MOVERATE = 2
flakespeed = 1
NBLINES = 1
NBSNOW = 90
PLAYERSIZE=3

MAXWIND = 0
SNOW_IMG = pygame.image.load("snowflake.png")
black = (0,0,0,255)
white = (255,255,255,255)
red = (255,0,0,255)

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
                 'y': WINHEIGHT-PLAYERSIZE,
                 'size': PLAYERSIZE,
                 'color' : (255,0,0),
                 'maxbullets': 2
                 }

    flakes = []
    for n in range(NBSNOW):
      flakes.append( newflake() )

 
    bullets = []
                 
    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False

     

    wind = random.randint(-MAXWIND, MAXWIND)

    while True: # main game loop
        pygame.draw.rect( DISPLAYSURF, black, (0,0,   WINWIDTH,WINHEIGHT ))
        if moveUp : player['y'] = player['y']-2
        if moveDown : player['y'] = player['y']+2
        if moveLeft : player['x'] = player['x']-2
        if moveRight : player['x'] = player['x']+2
        player['rect'] = pygame.Rect( (player['x'], player['y'], 2, 2) )

        for flake in flakes:
           
	        # Get flake new position
            new_x = flake['x'] + wind
            new_y = flake['y'] + random.randint(0,MAXSPEED)+(flakespeed)

	        # Make sure the flake stays on screen
            if new_x < 0:
                new_x += WINWIDTH
            if new_x >= WINWIDTH:
                new_x -= WINWIDTH


            # Clear flake
            
            
            flake['x'] = new_x
            flake['y'] = new_y
                
	        # Draw flake
            DISPLAYSURF.blit(SNOW_IMG, (flake['x'],flake['y'], flake['x']+50,flake['y']+50))
            flake['rect'] = pygame.Rect( (flake['x'], flake['y'], 40, 40) )
            
            if player['rect'].colliderect(flake['rect']):
                terminate()
                print('Collision')
           
            
	        # If the color is not black, we move the flake
            if new_y > WINHEIGHT:

	           # Otherwise, we move the flake back to the top
               flake['x'] = random.randint(0,WINWIDTH-1)
               flake['y'] = random.randint(-WINHEIGHT//2,0)
        for bullet in bullets:
			# Get bullet new position
            new_y = bullet['y'] - (bullet['speed'])

	        # Make sure the bullet stays on screen
            if new_y < 0:
				bullets.remove(bullet)
            else:	
                bullet['rect'] = pygame.Rect( (bullet['x'], bullet['y'], bullet['size'], bullet['size']) )
				
                for flake in flakes:
               
                  flake['rect'] = pygame.Rect( (flake['x'], flake['y'], 40, 40) )
            
                  if bullet['rect'].colliderect(flake['rect']):
                    flake['x'] = random.randint(0,WINWIDTH-1)
                    flake['y'] = random.randint(-WINHEIGHT//2,0)
                    bullets.remove (bullet)
                    for n in range (10):
                     flakes.append( newflake() )
                     flakes.append( newflake() )
                    
                    

            bullet['y']= new_y
                 
            pygame.draw.rect( DISPLAYSURF, bullet['color'], (bullet['x'], bullet['y'], bullet['size'], bullet['size'] ))


        pygame.draw.rect( DISPLAYSURF, red, (player['x'], player['y'], player['size'], player['size'] ))
           
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
					
                 if len(bullets)<player['maxbullets']:
                  bullets.append( {
                   'x': player['x'],
                   'y': player['y'],
                   'color' : white,
                   'size' : 3,
                   'speed' : 1,
                 } )

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

            
                     
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
        
def newflake():
     
    color = random.randint(192, 255)
    flake = {
                 'x': random.randint(0,WINWIDTH-1),
                 'y': random.randint(-WINHEIGHT,0),
                 'color' : (color,color,color),
                 }
    return flake
                 
if __name__ == '__main__':
    main()
