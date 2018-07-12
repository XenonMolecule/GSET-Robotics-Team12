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

def probe_direction():
    dist = sensorUltraSonic.value()
    # Turn Left
    motorDriveLeft.run_to_rel_pos(position_sp=-25, speed_sp = 100, stop_action="hold")
    motorDriveRight.run_to_rel_pos(position_sp=25, speed_sp = 100, stop_action="hold")
    if(dist < sensorUltraSonic.value()):
        return 0 # Target is left
    else:
        return 1 # Target is right

# Max_turn in ticks
def turn_to_wall(max_turn):
    last_dist = 100
    motorDriveLeft.run_to_rel_pos(position_sp=(-1 * max_turn), speed_sp = 100, stop_action="hold")
    motorDriveRight.run_to_rel_pos(position_sp=max_turn, speed_sp = 100, stop_action="hold")
    # Check for wall while turning left
    while sensorUltraSonic.value() < last_dist and (motorDriveLeft.state == "running" and motorDriveRight.state == "running"):
        last_dist = sensorUltraSonic.value()
        sleep(0.01)
    motorDriveLeft.stop(stop_action="brake")
    motorDriveRight.stop(stop_action="brake")
    if(sensorUltraSonic.value() < last_dist):
        sleep(0.1)
        motorDriveLeft.run_timed(time_sp=0.01, speed_sp=100, stop_action="brake")
        motorDriveRight.run_timed(time_sp=0.01, speed_sp=-100, stop_action="brake")
        return
    # Reset rotation to center
    motorDriveLeft.run_to_rel_pos(position_sp=max_turn, speed_sp = 100, stop_action="hold")
    motorDriveLeft.run_to_rel_pos(position_sp=(-1 * max_turn), speed_sp = 100, stop_action="hold")
    motorDriveLeft.wait_while("running")
    motorDriveRight.wait_while("running")
    motorDriveLeft.run_to_rel_pos(position_sp=max_turn, speed_sp = 100, stop_action="hold")
    motorDriveRight.run_to_rel_pos(position_sp=(-1 * max_turn), speed_sp = 100, stop_action="hold")
    # Check for wall while turning right
    while sensorUltraSonic.value() < last_dist and (motorDriveLeft.state == "running" and motorDriveRight.state == "running"):
        last_dist = sensorUltraSonic.value()
        sleep(0.01)
    motorDriveLeft.stop(stop_action="brake")
    motorDriveRight.stop(stop_action="brake")
    if(sensorUltraSonic.value() < last_dist):
        sleep(0.1)
        motorDriveLeft.run_timed(time_sp=0.01, speed_sp=-100, stop_action="brake")
        motorDriveRight.run_timed(time_sp=0.01, speed_sp=100, stop_action="brake")
        return
    motorDriveLeft.run_to_rel_pos(position_sp=(-1 * max_turn), speed_sp = 100, stop_action="hold")
    motorDriveRight.run_to_rel_pos(position_sp=(max_turn), speed_sp = 100, stop_action="hold")
    motorDriveLeft.wait_while("running")
    motorDriveRight.wait_while("running")

turn_to_wall(100)
