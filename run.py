#!/usr/bin/python3
"""Sample broken build alert"""

from time import sleep
from math import e
from numpy import linspace
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.set_rotation(180)

red = [255, 0, 0]
green = [0, 255, 0]
orange = [255, 165, 0]

def delay(t):
    """Defines delay function"""
    return 1 - e**(-t/3)

sense.low_light = False
sense.clear(green)
sleep(3)
sense.low_light = True
sleep(3)
sense.low_light = False
for t in linspace(1.0, 15.0, num = 5):
    print(t)
    print(delay(t))
    sense.clear(orange)
    sleep(delay(t))
    sense.clear()
    sleep(delay(t))

sense.show_message('frangosi broke the build', text_colour=[0,0,255], scroll_speed=0.05)
sense.clear(red)
sleep(10)
sense.low_light = True


