#!/usr/bin/python
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.low_light = True
sense.clear()

red = (255,0,0)

matrix = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

i = 0
k = 0
while (i < 64):
    # print "Iteration: ", k
    k += 1
    x = randint(0,7)
    y = randint(0,7)
    sleep(0.01)
    # print (x,y)
    if matrix[x][y] == 0:
        # print "HIT"
        matrix[x][y] = 1
        i += 1
        sense.set_pixel(x,y, red)
    # else:
        # print "MISS"

# print matrix
# red = (255,0,0)
# obstacles = [(2,3), (5,4), (6,3)]

# for xy in obstacles:
    # sense.set_pixel( xy[0], xy[1], red )
