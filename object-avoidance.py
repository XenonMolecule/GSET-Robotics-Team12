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

targetDistance = 70
speed = 300
time_in_range = 0

# Drive up to the obstacle
while True:
    speed = (targetDistance - sensorUltraSonic.value()) * 3
    motorDriveLeft.run_forever(speed_sp=max(50, min(900, speed)))
    motorDriveRight.run_forever(speed_sp=max(50, min(900, speed)))
    if(abs(speed) < 10)
        time_in_range+=0.1
        if(time_in_range > 1.5):
            break
    sleep(0.1)

motorDriveLeft.stop(stop_action="brake")
motorDriveRight.stop(stop_action="brake")

# Turn 90 degrees
motorDriveLeft.run_to_rel_pos(position_sp=236, speed_sp = 200, stop_action = "hold")
motorDriveRight.run_to_rel_pos(position_sp=-236, speed_sp = 200, stop_action = "hold")

motorDriveLeft.wait_while('running')
motorDriveRight.wait_while('running')

delay(0.5)

# Turn in a semicircle around the obstacle
motorDriveLeft.run_forever(speed_sp=300)
motorDriveRight.run_forever(speed_sp=900)
delay(1)

while sensorLight.value() > 375:
    motorDriveLeft.run_forever(speed_sp=300)
    motorDriveRight.run_forever(speed_sp=900)
    delay(0.1)

motorDriveLeft.stop(stop_action = "brake")
motorDriveRight.stop(stop_action = "brake")

delay(0.5)

# Turn 90 degrees back onto the line
motorDriveLeft.run_to_rel_pos(position_sp = -236, speed_sp = 200, stop_action= "hold")
motorDriveRight.run_to_rel_pos(position_sp = 236, speed_sp = 200, stop_action = "hold")
