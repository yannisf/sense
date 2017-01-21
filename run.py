#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()


color = [255, 0, 0]
sense.clear(color)
sleep(1)
sense.show_message('frangosi broke the build', text_colour=[0,0,255], scroll_speed=0.05)
sense.clear(color)



