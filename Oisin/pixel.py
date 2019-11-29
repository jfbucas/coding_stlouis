import random, sys, time, math, pygame
from pygame.locals import *
from pygame import gfxdraw



FPS = 60 # frames per second to update the screen
WINWIDTH = 1090 # width of the program's window, in pixels
WINHEIGHT = 745 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
MOVERATE = 5
MOVERATEFORENEMY=4
NB_ENEMY = 15
INVULNTIME = 5


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG, GRASSIMAGES

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Pixel')
    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    while True:
        runGame()


def runGame():

    player = {
	             'x': HALF_WINWIDTH,
                 'y': HALF_WINHEIGHT,
	             'previousx': HALF_WINWIDTH,
                 'previousy': HALF_WINHEIGHT,
                 'color': (255,0,0),
                 'colorinvulnerable': (0,255,0),
                 'invulnerable' : False,
                 }

    enemy = []
    for i in range(NB_ENEMY):
         enemy.append( {'x': random.randint(0,WINWIDTH),
                     'y': random.randint(0,WINHEIGHT),
                 'color': (255,0,255),
                 })



    moveLeft  = False
    moveRight = False
    moveUp    = False
    moveDown  = False
    MOVERATE = 5
    MYTICKCOUNTERMAX = 100
    tickcounter=0
    while True: # main game loop
        if tickcounter > MYTICKCOUNTERMAX:
          pygame.draw.rect(DISPLAYSURF, (0,0,0),(0,0,WINWIDTH,WINHEIGHT))
          tickcounter = -1000
		
        for e in enemy:
            gfxdraw.pixel(DISPLAYSURF, e['x'], e['y'], e['color'])
            
        if player['invulnerable'] > 0:
           player['invulnerable'] -= 1
           #gfxdraw.pixel(DISPLAYSURF, player['x'], player['y'], player['colorinvulnerable'])
           pygame.draw.line(DISPLAYSURF, player['colorinvulnerable'], [player['previousx'], player['previousy']], [player['x'], player['y']])
        else:
           #gfxdraw.pixel(DISPLAYSURF, player['x'], player['y'], player['color'])
           pygame.draw.line(DISPLAYSURF, player['color'], [player['previousx'], player['previousy']], [player['x'], player['y']])
        
        
        for event in pygame.event.get(): # event handling loop
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
                elif event.key == K_r:
                    return

            elif event.type == KEYUP:
                # stop moving the player's squirrel
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
        player['previousx' ] = player['x']
        player['previousy' ] = player['y']
        if moveLeft:
            player['x'] -= MOVERATE
        if moveRight:
            player['x'] += MOVERATE
        if moveUp:
            player['y'] -= MOVERATE
        if moveDown:
            player['y'] += MOVERATE


        for e in enemy:

         if e['x'] > player['x']:
			e['x'] -= 1
         elif e['x'] < player['x']:
			e['x'] += 1
         if e['y'] > player['y']:
			e['y'] -= 1
         elif e['y'] < player['y']:
			e['y'] += 1

#         if DISPLAYSURF.get_at( (e['x'], e['y']) ) == player['color']:
         if ( e['x'], e['y']) == (player['x'], player['y']):
            e['x'] = random.randint(0,WINWIDTH)
            e['y'] = random.randint(0,WINHEIGHT)
            MOVERATE -= 1
            player['invulnerable'] = INVULNTIME * FPS
         if DISPLAYSURF.get_at( (e['x'], e['y']) ) == enemy[0]['color']:
            e['x'] = random.randint(0,WINWIDTH)
            e['y'] = random.randint(0,WINHEIGHT)
         #enemy['x'] += random.randint(-1,1)
         #enemy['y'] += random.randint(-1,1)
         if MOVERATE == 0:terminate()
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        tickcounter += 1



if __name__ == '__main__':
    main()

