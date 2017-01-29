#!/usr/bin/python3
"""
Generate points for a 3D grid
"""
from math import sin, cos
from sense_hat import SenseHat
from continuum import get_color

def z(x, y, t): # pylint: disable=I0011,W0613
    """The z point"""
    return int(100*sin(x-t) * cos(y-t)) + 156

def prepare_matrix(t=0):
    """
    Constructs an intensity pixel matrix for sense using enclosing function logic.
    """
    array = []
    for x in range(8):
        row = []
        for y in range(8):
            intensity = z(x, y, t)
            # red_intensity = intensity
            # green_intensity = intensity
            # blue_intensity = intensity
            # row.append((red_intensity, green_intensity, blue_intensity))
            row.append(get_color(intensity, 0, 255))
        array.append(row)
    return sum(array, [])

sense = SenseHat()
sense.clear()
sense.low_light = False
sense.set_rotation(180)

time_value = 0
while True:
    sense.set_pixels(prepare_matrix(time_value))
    time_value += 0.01
