import random, sys, time, math, pygame
from pygame.locals import *

from pygame import gfxdraw


FPS = 60 # frames per second to update the screen
WINWIDTH = 1090 # width of the program's window, in pixels
WINHEIGHT = 1045 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 7752)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

MOVERATE = 1

NBLINES = 1
NBSNOW = 1

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('hi')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

   
    while True:
        runGame()
   
def terminate():
    pygame.quit()
    sys.exit()
   
def runGame():
    random.seed(time.time())
   
    player = {
                 'x': HALF_WINWIDTH,
                 'y': HALF_WINHEIGHT,
                 'color' : (255,255,255),
                 }
                
                 
    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False

    while True: # main game loop


        for n in range(NBSNOW):
            gfxdraw.pixel(DISPLAYSURF, random.randint(0,WINWIDTH),random.randint(0,WINHEIGHT),
                [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
                )

		
        gfxdraw.pixel(DISPLAYSURF, player['x'], player['y'], player['color'])
 
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
