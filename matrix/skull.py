#!/usr/bin/python
"""
Paint a skull on the matrix
"""
from random import randint
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

def render(X, O):
    """
    Render the matrix
    """

    skull = [
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, X, O,
    O, X, X, X, X, X, X, X,
    O, X, O, O, X, O, O, X,
    O, X, X, X, X, X, X, X,
    O, X, X, X, O, X, X, X,
    O, O, X, X, X, X, X, O,
    O, O, X, O, X, O, X, O
    ]

    sense.set_pixels(skull)

skull_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
background = [0, 0, 0]
render(skull_color, background)
