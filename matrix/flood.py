#!/usr/bin/python3
"""
Renders a matrix in time
"""
from numpy import linspace
from sense_hat import SenseHat

def clamp(value, max_value=255):
    return min(value, max_value)

sense = SenseHat()
# sense.set_rotation(180)

matrix1 = [
    1, 1, 2, 3, 4, 5, 6, 7,
    1, 2, 3, 4, 5, 6, 7, 8,
    2, 3, 4, 5, 6, 7, 8, 9,
    3, 4, 5, 6, 7, 8, 9, 10,
    4, 5, 6, 7, 8, 9, 10, 10,
    5, 6, 7, 8, 9, 10, 11, 12,
    6, 7, 8, 9, 10, 11, 12, 13,
    7, 8, 9, 10, 11, 12, 13, 14
    ]

matrix2 = [
    1, 1, 1, 1, 1, 1, 1, 1,
    2, 2, 2, 2, 2, 2, 2, 2,
    3, 3, 3, 3, 3, 3, 3, 3,
    4, 4, 4, 4, 4, 4, 4, 4,
    5, 5, 5, 5, 5, 5, 5, 5,
    6, 6, 6, 6, 6, 6, 6, 6,
    7, 7, 7, 7, 7, 7, 7, 7,
    8, 8, 8, 8, 8, 8, 8, 8,
    ]


while True:
    sense.clear()
    for t in linspace(0, 255, num=1000):
        next_matrix = [None]*64
        for i in range(64):
            # print("i=%d" % i)
            intensity = clamp(int(matrix1[i] * t))
            next_matrix[i] = [intensity, 0, 0]
        sense.set_pixels(next_matrix)
    # print(next_matrix)
    # print("\n")
