#!/usr/bin/python
import termios, fcntl, sys, os
from sense_hat import SenseHat
import random
 
sense = SenseHat()
sense.clear()
sense.rotation = 180
 
fd = sys.stdin.fileno()
 
oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)
 
oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
 
try:
    while 1:
        try:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            c = sys.stdin.read(1)
            print "Got character {} with colour R:{}, G:{}, B:{}".format(repr(c), r, g, b)
            sense.show_letter(str(c), text_colour=[r, g, b])
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
