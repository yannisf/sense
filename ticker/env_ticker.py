#!/usr/bin/python3
import sys
from sense_hat import SenseHat
from time import sleep
from datetime import date

sense = SenseHat()
sense.clear()
sense.set_rotation(180)
scroll_speed = 0.1

while True:
    temp = str(int(sense.get_temperature()))
    hum = str(int(sense.get_humidity()))
    press = str(int(sense.get_pressure()))
    today = date.today().strftime("%d/%m/%Y")
    sense.show_message(text_string=f'{today}  {temp}C  {hum}%  {press}hPa', scroll_speed=scroll_speed)
    sleep(5)

