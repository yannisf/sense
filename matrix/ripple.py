#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep

factors = [0.05, 0.20, 0.35, 0.50, 0.65, 0.70, 0.85, 1.00]

sense = SenseHat()
sense.clear()

X = [255, 255, 255]

matrix = [
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X,
X, X, X, X, X, X, X, X
]

sense.set_pixels(matrix)
