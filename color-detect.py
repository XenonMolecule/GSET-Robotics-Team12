#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
sensorColor = ColorSensor()

lcd = Screen()

# Initialization
sensorLight.mode = "REFLECT"
sensorColor.mode = "COL-COLOR"

colors=('unknown','black','blue','green','yellow','red','white','brown')

while True:
    if sensorColor.value() == 3:
        Leds.set_color(Leds.LEFT,  Leds.GREEN)
        Sound.speak("Ya like Jazz?")
    else:
        Leds.set_color(Leds.LEFT, Leds.ORANGE)
    sleep(1)
