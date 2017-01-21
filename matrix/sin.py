#!/usr/bin/python3
"""LED matrix sinusoidal pulse"""

from time import sleep
from math import sin
from numpy import linspace
from sense_hat import SenseHat

sense = SenseHat()

sense.clear()
sense.low_light = False

def f(x):
    """Defines the intensity function over time"""
    return int(255 * (sin(10 * x**2) / 2.1 + 0.52))

for t in linspace(0.0, 4.965, num=3000):
    red_intensity = f(t)
    print("r=%d" % (red_intensity))
    color = [red_intensity, 0, 0]
    sense.clear(color)
    sleep(0.001)
