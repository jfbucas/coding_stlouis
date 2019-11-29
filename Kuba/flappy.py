"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.

"""

from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)
balls = []

def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(1, 50)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'purple')
    else:
        dot(10, 'white')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(50, 'purple')

    update()

def move():
    "Update object positions."
    bird.y -= 5

def draw():
    "Draw game and move lazer."
    clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    for boss in bosses:
        ball.x -= 5

    if randrange(10) == 0:
        y = randrange(-240, 240)
        ball = vector(199, y)
        balls.append(ball)
    for ball in balls:
        ball.x -= 5

    if randrange(10) == 0:
        y = randrange(-240, 240)
        ball = vector(199, y)
        balls.append(ball)

    while len(bosses) > 0 and not inside(bosses[0]):
        bosses.pop(0)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for boss in bosses:
        if abs(boss - bird) < 1:
            draw(False)
            return

    for ball in balls:
        if abs(ball - bird) < 20:
            draw(False)
            return

    draw(True)
    ontimer(move, 15)

setup(550, 550, 430, 60)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
