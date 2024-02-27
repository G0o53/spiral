# import turtle art as t
import turtle as t

# the random number generator
from random import randint


t.bgcolor('black')
t.speed('fast')
t.pensize(2)

for x in range(400):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    t.colormode(255)
    t.pencolor(r, g, b)

    t.forward(50 + x)
    t.right(91)

t.hideturtle()