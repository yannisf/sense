#!/usr/bin/python
from sense_hat import SenseHat
from random import randint

sense = SenseHat()

def render(X, O):
    heart = [
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, X, O,
    O, X, X, X, X, X, X, X,
    O, X, O, O, X, O, O, X,
    O, X, X, X, X, X, X, X,
    O, X, X, X, O, X, X, X,
    O, O, X, X, X, X, X, O,
    O, O, X, O, X, O, X, O
    ]

    sense.set_pixels(heart)

heart_color = [randint(0,255), randint(0,255), randint(0,255)]
background = [0,0,0]
heart_color = [randint(0,255), randint(0,255), randint(0,255)]
render(heart_color, background)
