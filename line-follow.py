#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
#sensorColor = ColorSensor()

#lcd = Screen()

colorValTotal = 0
colorValAvg = 0
previousColorAvg = 0
i = 0
numLoops = 0

# Initialization
sensorLight.mode = "REFLECT"
#sensorColor.mode = "COL-REFLECT"
whiteIntensity = 600
targetIntensity = 350
blackIntensity = 280

# Start Line Following
# TODO: CHANGE FROM TRUE TO CONDITION
leftSpeed = 300 # Speed of Left Motor
rightSpeed = 300 # Speed of Right Motor
speedModif = 0 # Speed Modifier for Motors
KP = 2 # P constant for PID

while True:
    i += 1

    if i <= 10:
        colorValTotal += sensorLight.value()
    else:
        numLoops += 1
        colorValAvg /= 10
        previousColorAvg = colorValAvg
        # lcd.clear()
        speedModif = int(KP * (sensorLight.value() - targetIntensity))
        if speedModif < 0:
            speedModif *= 2

        if numLoops != 0:
            if colorValAvg - previousColorAvg <= 0:
                #shift the robot to the left
                motorDriveLeft.run_forever(speed_sp=max(200, min(900, leftSpeed + speedModif)))
                motorDriveRight.run_forever(speed_sp=max(200, min(900, rightSpeed - speedModif)))
            elif colorValAvg - previousColorAvg > 0:
                #shift the robot to the right
                motorDriveLeft.run_forever(speed_sp=max(200, min(900, leftSpeed + speedModif)))
                motorDriveRight.run_forever(speed_sp=max(200, min(900, rightSpeed - speedModif)))

        motorDriveLeft.run_forever(speed_sp=max(200, min(900, leftSpeed + speedModif)))
        motorDriveRight.run_forever(speed_sp=max(200, min(900, rightSpeed - speedModif)))
        # lcd.draw.text((48,13), str(sensorLight.value())
        # lcd.update()
        colorValAvg = 0


