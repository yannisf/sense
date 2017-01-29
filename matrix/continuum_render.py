#!/usr/bin/python3
"""
Renders an RGB continuum in the LED matrix
"""
from time import sleep
from sense_hat import SenseHat
from continuum import get_color

sense = SenseHat()
sense.clear()
sense.low_light = False
sense.set_rotation(180)


color = get_color(0, 0, 20)
print(color)
color = get_color(20, 0, 20)
print(color)

for i in range(20):
    color = get_color(i, 0, 20)
    matrix = []
    for t in range(64):
        matrix.append(color)
    sense.set_pixels(matrix)
    sleep(0.5)
