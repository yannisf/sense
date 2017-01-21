#!/usr/bin/python

import numpy as np
from sense_hat import SenseHat
from time import sleep

x1 = 136
y1 = 45
z1 = 96

x2 = 43
y2 = 130
z2 = 58

def x(t):
    return int(round((x1 + (x2-x1)*t), 0))

def y(t):
    return int(round((y1 + (y2-y1)*t), 0))

def z(t):
    return int(round((z1 + (z2-z1)*t), 0))

sense = SenseHat()
sense.clear()
sense.low_light = False

while True:
    for t in np.arange(0.2, 1, 0.01):
        color = (x(t), y(t), z(t))
        # print color
        sense.clear(color)
        sleep(0.05)
    for t in np.arange(1, 0.2, -0.01):
        color = (x(t), y(t), z(t))
        # print color
        sense.clear(color)
        sleep(0.05)
