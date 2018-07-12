#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from time import time

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
sensorColor = ColorSensor()
sensorUltraSonic = UltrasonicSensor()

lcd = Screen()

# Initialization
sensorLight.mode = "REFLECT"
sensorColor.mode = "COL-COLOR"
sensorUltraSonic.mode = "US-DIST-IN"
targetIntensity = 375


# Start Line Following
# Constants work with 7.77 Volts on Battery
leftSpeed = 100 # Speed of Left Motor
rightSpeed = 100 # Speed of Right Motor
speedModif = 0 # Speed Modifier for Motors
KP = 2.5 # P constant for PID
K_Whippage_B = 0.65 # Constant for Whippage on Line
K_Whippage_W = 1.75 # Constant for Whippage off Line
lastVictimTime = 0.0 # The time at which the last victim was rolled over
recentVictim = False # Whether or not the robot detected a victim recently
avoided_object = False

def object_avoidance():
    targetDistance = 45
    speed = 300
    time_in_range = 0
    turn_90 = 236

    # Drive up to the obstacle
    while True:
        speed = (sensorUltraSonic.value() - targetDistance) * 3
        if(speed < 0):
            motorDriveLeft.run_forever(speed_sp=max(-900, min(-50, speed)))
            motorDriveRight.run_forever(speed_sp=max(-900, min(-50, speed)))
        else:
            motorDriveLeft.run_forever(speed_sp=max(50, min(900, speed)))
            motorDriveRight.run_forever(speed_sp=max(50, min(900, speed)))
        if(abs(speed) < 10):
            time_in_range+=0.1
            if(time_in_range > 1.5):
                break
        sleep(0.1)

    motorDriveLeft.stop(stop_action="brake")
    motorDriveRight.stop(stop_action="brake")

    # Turn 90 degrees
    motorDriveLeft.run_to_rel_pos(position_sp=-1 * turn_90, speed_sp = 200, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp=turn_90, speed_sp = 200, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    sleep(0.5)

    # Turn in a semicircle around the obstacle
    motorDriveLeft.run_forever(speed_sp=682)
    motorDriveRight.run_forever(speed_sp=300)
    sleep(1)

    while sensorLight.value() > 375:
        motorDriveLeft.run_forever(speed_sp=682)
        motorDriveRight.run_forever(speed_sp=300)
        sleep(0.1)

    motorDriveLeft.stop(stop_action = "brake")
    motorDriveRight.stop(stop_action = "brake")

    sleep(0.5)

    # Turn 90 degrees back onto the line
    motorDriveLeft.run_to_rel_pos(position_sp = -1 * turn_90, speed_sp = 200, stop_action= "hold")
    motorDriveRight.run_to_rel_pos(position_sp = turn_90, speed_sp = 200, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

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

    if(sensorUltraSonic.value() < 50 and not avoided_object):
        object_avoidance()
        avoided_object = True

    # Let Eggbert sleep just a tad
    sleep(0.1)
