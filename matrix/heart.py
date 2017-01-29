#!/usr/bin/python
from sense_hat import SenseHat
from random import randint

sense = SenseHat()
sense.rotation = 180


def render(X, O):
    heart = [
    O, O, O, O, O, O, O, O,
    O, X, X, O, X, X, O, O,
    X, X, X, X, X, X, X, O,
    X, X, X, X, X, X, X, O,
    O, X, X, X, X, X, O, O,
    O, O, X, X, X, O, O, O,
    O, O, O, X, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]

    print(heart)
    sense.set_pixels(heart)

heart_color = [randint(0,255), randint(0,255), randint(0,255)]
background = [randint(0,255), randint(0,255), randint(0,255)]
#while True:
#    event = sense.stick.wait_for_event()
#    print event.direction
#    if event.direction == 'up':
heart_color = [randint(0,255), randint(0,255), randint(0,255)]
render(heart_color, background)
#    elif event.direction == 'down':
#        background = [randint(0,255), randint(0,255), randint(0,255)]
#        render(heart_color, background)
