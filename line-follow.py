#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
#sensorColor = ColorSensor()

lcd = Screen()

# Initialization
sensorLight.mode = "REFLECT"
#sensorColor.mode = "COL-COLOR"
whiteIntensity = 600
targetIntensity = 375
blackIntensity = 280

# Start Line Following
# TODO: CHANGE FROM TRUE TO CONDITION
leftSpeed = 100 # Speed of Left Motor
rightSpeed = 100 # Speed of Right Motor
speedModif = 0 # Speed Modifier for Motors
KP = 1.0 # P constant for PID
lastVictimTime = 0.0

while True:
    #lcd.clear()
    speedModif = int(KP * (sensorLight.value() - targetIntensity))
    if speedModif < 0:
        speedModif *= 4
    else:
        speedModif *= 1
    motorDriveLeft.run_forever(speed_sp=max(-100, min(900, leftSpeed + speedModif)))
    motorDriveRight.run_forever(speed_sp=max(-100, min(900, rightSpeed - speedModif)))
    #lcd.draw.text((48,13), str(sensorLight.value())
    #lcd.update()

    '''if sensorColor.value() == 3:
        Leds.set_color(Leds.LEFT,  Leds.GREEN)
        if lastVictimTime > 3:
            Sound.beep()
            lastVictimTime = 0
        else:
            lastVictimTime += 0.1
    else:
        Leds.set_color(Leds.LEFT, Leds.ORANGE)
    '''
    sleep(0.1)
