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
sensorColor.mode = "COL-REFLECT"
whiteIntensity = 600
targetIntensity = 350
blackIntensity = 280

# Start Line Following
# TODO: CHANGE FROM TRUE TO CONDITION
leftSpeed = 200 # Speed of Left Motor
rightSpeed = 200 # Speed of Right Motor
speedModif = 0 # Speed Modifier for Motors
KP = 2.5 # P constant for PID
while True:
    #lcd.clear()
    speedModif = int(KP * (sensorLight.value() - targetIntensity))
    if speedModif < 0:
        speedModif *= 6
    else:
        speedModif *= 1
    motorDriveLeft.run_forever(speed_sp=max(100, min(900, leftSpeed - speedModif)))
    motorDriveRight.run_forever(speed_sp=max(100, min(900, rightSpeed + speedModif)))
    #lcd.draw.text((48,13), str(sensorLight.value())
    #lcd.update()
    sleep(0.1)
