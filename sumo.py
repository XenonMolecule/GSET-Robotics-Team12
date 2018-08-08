#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from time import time

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
sensorColor = ColorSensor()
sensorUltraSonic = UltrasonicSensor()
sensorTouch = TouchSensor()

lcd = Screen()

# Initialization
sensorLight.mode = "REFLECT"
sensorColor.mode = "COL-REFLECT"
sensorUltraSonic.mode = "US-DIST-CM"
whiteThreshLight = 300
whiteThreshColor = 6
speedLeft = 0
speedRight = 0

btn = Button()
Leds.set_color(Leds.LEFT, Leds.AMBER)
Leds.set_color(Leds.RIGHT, Leds.AMBER)
while not btn.enter:
    sleep(0.1)
Leds.set_color(Leds.LEFT, Leds.GREEN)
Leds.set_color(Leds.RIGHT, Leds.GREEN)
sleep(5)

def spin_around():
    motorDriveLeft.run_timed(time_sp = 500, speed_sp = -500)
    motorDriveRight.run_timed(time_sp = 500, speed_sp = -500)

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = -472, speed_sp = 400, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 472, speed_sp = 400, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

while(True):
    # Base Speed Values
    speedLeft = 350
    speedRight = 350

    if(sensorUltraSonic.value() < 400):
        speedLeft = 1000
        speedRight = 1000

    # Hit From Behind
    if(sensorTouch.value()):
        speedLeft = -1000
        speedRight = -1000

    # Left Sensor on Line
    if(sensorColor.value() > whiteThreshColor):
        speedLeft = -600
        if(speedRight > 0):
            speedRight /= 2

    # Right Sensor on Line
    if(sensorLight.value() > whiteThreshLight):
        speedRight = -600
        if(speedLeft > 0):
            speedLeft /= 2

    # On White Line
    if (sensorLight.value() > whiteThreshLight) and (sensorColor.value() > whiteThreshColor):
        spin_around()


    motorDriveLeft.run_forever(speed_sp=speedLeft)
    motorDriveRight.run_forever(speed_sp=speedRight)
    sleep(0.1)

motorDriveLeft.stop(stop_action = "brake")
motorDriveRight.stop(stop_action = "brake")
