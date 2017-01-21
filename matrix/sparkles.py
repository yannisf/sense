#!/usr/bin/python
from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(15, 255)
    g = randint(15, 255)
    b = randint(15, 255)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.005)

