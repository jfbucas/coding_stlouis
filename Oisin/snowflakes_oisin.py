import random, sys, time, math, pygame
from pygame.locals import *

from pygame import gfxdraw


FPS = 60 # frames per second to update the screen
WINWIDTH = 1090 # width of the program's window, in pixels
WINHEIGHT = 1045 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

MOVERATE = 1

NBLINES = 1
NBSNOW = 1

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
                 'color' : (255,0,255),
                 }
                
    lines = []
    for i in range(NBLINES):
        lines.append({
                 'a': [random.randint(0,HALF_WINWIDTH),random.randint(0,HALF_WINHEIGHT)],
                 'b': [random.randint(0,HALF_WINWIDTH),random.randint(0,HALF_WINHEIGHT)],
                 'dira' : [random.randint(-1,2), random.randint(-1,2)],
                 'dirb' : [random.randint(-1,2), random.randint(-1,2)],
                 'color' : [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)],
                 'dircolor' : [random.randint(-1,2), random.randint(-1,2), random.randint(-1,2)]
                 })
                 
    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False

    while True: # main game loop


        for n in range(NBSNOW):
            gfxdraw.pixel(DISPLAYSURF, random.randint(0,WINWIDTH),random.randint(5,10),
                [random.randint(250,255 ),random.randint(250, 255),random.randint(0250, 255)]
                )

		
        gfxdraw.pixel(DISPLAYSURF, player['x'], player['y'], player['color'])
        #for line in lines:
        #    pygame.draw.line(DISPLAYSURF, line['color'], line['a'],  line['b'])
        #gfxdraw.pixel(DISPLAYSURF, enemy['x'], enemy['y'], enemy['color'])
		
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
            
        
        for line in lines:
            line['a'][0] += line['dira'][0]
            line['a'][1] += line['dira'][1]
    
            line['b'][0] += line['dirb'][0]
            line['b'][1] += line['dirb'][1]
            
            
            if line['a'][0] < 0:
                line['dira'][0] = -line['dira'][0] 
            if line['a'][0] > WINWIDTH:
                line['dira'][0] = -line['dira'][0] 
    
    
            if line['b'][0] < 0:
                line['dirb'][0] = -line['dirb'][0] 
            if line['b'][0] > WINWIDTH:
                line['dirb'][0] = -line['dirb'][0] 
    
    
            if line['a'][1] < 0:
                line['dira'][1] = -line['dira'][1] 
            if line['a'][1] > WINHEIGHT:
                line['dira'][1] = -line['dira'][1] 
    
    
            if line['b'][1] < 0:
                line['dirb'][1] = -line['dirb'][1] 
            if line['b'][1] > WINHEIGHT:
                line['dirb'][1] = -line['dirb'][1] 
    


            line['color'][0] += line['dircolor'][0]
            line['color'][1] += line['dircolor'][1]
            line['color'][2] += line['dircolor'][2]

    
            if line['color'][0] < 0:
                line['dircolor'][0] = random.randint(-1,2)
                line['color'][0] = 0
            if line['color'][1] < 0:
                line['dircolor'][1] = random.randint(-1,2)
                line['color'][1] = 0
            if line['color'][2] < 0:
                line['dircolor'][2] = random.randint(-1,2)
                line['color'][2] = 0
    
            if line['color'][0] > 255:
                line['dircolor'][0] = random.randint(-1,2)
                line['color'][0] = 255                
            if line['color'][1] > 255:
                line['dircolor'][1] = random.randint(-1,2)
                line['color'][1] = 255                
            if line['color'][2] > 255:
                line['dircolor'][2] = random.randint(-1,2)
                line['color'][2] = 255
    
    

                    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
     
if __name__ == '__main__':
    main()
