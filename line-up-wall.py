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
sensorUltraSonic.mode = "US-DIST-CM"

def probe_direction():
    dist = sensorUltraSonic.value()
    # Turn Left
    motorDriveLeft.run_to_rel_pos(position_sp=-35, speed_sp = 50, stop_action="hold")
    motorDriveRight.run_to_rel_pos(position_sp=35, speed_sp = 50, stop_action="hold")
    motorDriveLeft.wait_while("running")
    motorDriveRight.wait_while("running")
    sleep(0.2)
    new_dist = sensorUltraSonic.value()
    sleep(0.2)
    motorDriveLeft.run_to_rel_pos(position_sp=35, speed_sp = 50, stop_action="hold")
    motorDriveRight.run_to_rel_pos(position_sp=-35, speed_sp = 50, stop_action="hold")
    motorDriveLeft.wait_while("running")
    motorDriveRight.wait_while("running")
    if(new_dist < dist):
        return 0 # Target is left
    else:
        return 1 # Target is right

# Max_turn in ticks
def turn_to_wall(max_turn):
    last_dist = 1000
    direction = probe_direction()
    times_increasing = 0 # times increasing in a row
    if(direction == 0):
        motorDriveLeft.run_forever(speed_sp = -75)
        motorDriveRight.run_forever(speed_sp = 75)
        sleep(0.5)
        # Check for wall while turning left
        while True:
            print(sensorUltraSonic.value())
            if (sensorUltraSonic.value() >= last_dist):
                times_increasing += 1
            else:
                times_increasing = 0
            if (times_increasing > 0):
                break
            last_dist = sensorUltraSonic.value()
            sleep(0.1)
        motorDriveLeft.stop(stop_action="hold")
        motorDriveRight.stop(stop_action="hold")
    else:
        motorDriveLeft.run_forever(speed_sp = 75)
        motorDriveRight.run_forever(speed_sp = -75)
        sleep(0.5)
        # Check for wall while turning right
        while True:
            print(sensorUltraSonic.value())
            if (sensorUltraSonic.value() >= last_dist):
                times_increasing += 1
            else:
                times_increasing = 0
            if (times_increasing > 0):
                break
            last_dist = sensorUltraSonic.value()
            sleep(0.1)
        motorDriveLeft.stop(stop_action="hold")
        motorDriveRight.stop(stop_action="hold")

turn_to_wall(500)

sleep(5)
