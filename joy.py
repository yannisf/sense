from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
from random import randint

x = 3
y = 3
sense = SenseHat()

color = [255, 0, 0]

def clamp(value, min_value=0, max_value=7):
    #return min(max_value, max(min_value, value))
    return value % 8

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def update_color(event):
	print ("Updating color!")
	global color
	color = [randint(0,255), randint(0,255), randint(0,255)]

def refresh():
    sense.clear()
    sense.set_pixel(x, y, color)
    print ("Color is: ", color)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = update_color
sense.stick.direction_any = refresh
refresh()
pause()
