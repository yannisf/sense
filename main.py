#!/usr/bin/python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
# sense.low_light = True
sense.low_light = False

for z in range (0, 255, 16):
    for y in range(0,255, 16):
        if y % 2 == 0:
            # print("up")
            for x in range(255):
                # sleep(0.05)
                # print(x,y)
                color = (x,y,z)
                sense.clear(color)
        else:
            # print("down")
            for x in range(255,0, -16):
                # sleep(0.05)
                # print(x,y)
                color = (x,y,z)
                sense.clear(color)

sense.clear()
