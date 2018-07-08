#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
#sensorColor = ColorSensor()

#lcd = Screen()

# Initialization
sensorLight.mode = "REFLECT"
#sensorColor.mode = "COL-REFLECT"

kP = 2
targetIntensity = 375
correction = 0
leftSpeed = 0
rightSpeed = 0

while True:
    lightIntensity = sensorLight.value()

    correction = kP * (lightIntensity - targetIntensity)

    if correction <= 0:
        #shift bot to left
        motorDriveLeft.run_forever(speed_sp=max(50, min(900, leftSpeed - correction)))
        motorDriveRight.run_forever(speed_sp=max(50, min(900, rightSpeed + correction)))
    else:
        #shift bot to right
        motorDriveLeft.run_forever(speed_sp=max(50, min(900, leftSpeed + correction)))
        motorDriveRight.run_forever(speed_sp=max(50, min(900, rightSpeed - correction)))
