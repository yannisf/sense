#!/usr/bin/python3
"""
Get information from environment sensors
"""

import sys
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
#sense.set_rotation(180)
scroll_speed = 0.06

raw_name = sys.argv[0]
slash_index = raw_name.rfind("/")
name = raw_name[slash_index+1:]
print("script: %s" % name)

sense.show_message(name)

while True:
    humidity = str(int(sense.get_humidity()))
    pressure = str(int(sense.get_pressure()))

    temperature = str(int(sense.get_temperature()))
    temperature_from_humidity = str(int(sense.get_temperature_from_humidity()))
    temperature_from_pressure = str(int(sense.get_temperature_from_pressure()))

    sense.show_message(text_string="Hum: " + humidity + "%", scroll_speed=scroll_speed)
    sense.show_message(text_string="Press: " + pressure, scroll_speed=scroll_speed)
    sense.show_message(text_string="Temp: " + temperature + "C", scroll_speed=scroll_speed)
    sense.show_message(text_string="Temp(hum): " + temperature_from_humidity + "C", scroll_speed=scroll_speed)
    sense.show_message(text_string="Temp(press): " + temperature_from_humidity + "C", scroll_speed=scroll_speed)
