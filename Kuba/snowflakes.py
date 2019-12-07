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

NBLINES = 1
NBSNOW = 100

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
    random.seed(time.time())
   
    player = {
                 'x': HALF_WINWIDTH,
                 'y': HALF_WINHEIGHT,
                 'color' : (255,0,0),
                 }

    flakes = []
    for n in range(NBSNOW):
      color = random.randint(128, 255)
      flakes.append( {
                 'x': random.randint(0,WINWIDTH-10),
                 'y': 5,
                 'color' : (color,color,color),
                 } )
                
                  
    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False

    pygame.draw.rect(DISPLAYSURF, (255,255,255),(0,WINHEIGHT-(MAXSPEED*3),WINWIDTH,WINHEIGHT))


    while True: # main game loop

        
        for n in range(NBSNOW):
            gfxdraw.pixel(DISPLAYSURF, flakes[n]['x'], flakes[n]['y'], [0,0,0])
            flakes[n]['y'] += random.randint(0,MAXSPEED)+1

            if DISPLAYSURF.get_at( [flakes[n]['x'],flakes[n]['y']] ) == (255,255,255):
               gfxdraw.pixel(DISPLAYSURF, flakes[n]['x'], flakes[n]['y'], flakes[n]['color'])
               flakes[n]['y'] = 5
                
            gfxdraw.pixel(DISPLAYSURF, flakes[n]['x'], flakes[n]['y'], flakes[n]['color'])

		
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
