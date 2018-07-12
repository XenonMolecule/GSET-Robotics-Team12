#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from time import time

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
sensorColor = ColorSensor()

lcd = Screen()

# Initialization
sensorLight.mode = "REFLECT"
sensorColor.mode = "COL-COLOR"
targetIntensity = 375


# Start Line Following
leftSpeed = 100 # Speed of Left Motor
rightSpeed = 100 # Speed of Right Motor
speedModif = 0 # Speed Modifier for Motors
KP = 2.5 # P constant for PID
K_Whippage_B = 0.65 # Constant for Whippage on Line
K_Whippage_W = 1.75 # Constant for Whippage off Line
lastVictimTime = 0.0 # The time at which the last victim was rolled over
recentVictim = False # Whether or not the robot detected a victim recently

# TODO: CHANGE FROM TRUE TO CONDITION
while True:
    # Use P-Loop to scale the speed modifier based on offset from optimal intensity
    speedModif = int(KP * (sensorLight.value() - targetIntensity))
    if speedModif < 0:
        speedModif *= K_Whippage_B # Increase whippage when on black lines
        speedModif = int(speedModif)
    else:
        speedModif *= K_Whippage_W # Modify whippage on white space
        speedModif = int(speedModif)

    # Run the motors with the modifications and within the desired speed range
    motorDriveLeft.run_forever(speed_sp=max(-100, min(900, leftSpeed + speedModif)))
    motorDriveRight.run_forever(speed_sp=max(-100, min(900, rightSpeed - speedModif)))

    # If we have detected some victims lately
    if time() - lastVictimTime < 2:
        recentVictim = True
    else:
        recentVictim = False

    # If we haven't detected any victims lately
    if not recentVictim:
        # If the robot detects a green line (victim)
        if sensorColor.value() == 3:
            Sound.beep()
            lastVictimTime = time() # Reset the victim timer

    # Let Eggbert sleep just a tad
    sleep(0.1)
