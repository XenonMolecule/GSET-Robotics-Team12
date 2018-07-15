#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from time import time

motorDriveLeft = LargeMotor("outA")
motorDriveRight = LargeMotor("outD")

sensorLight = LightSensor()
sensorColor = ColorSensor()
sensorUltraSonic = UltrasonicSensor()
sensorIR = Sensor(address='in2:i2c8',driver_name='ht-nxt-ir-seek-v2')

lcd = Screen()

def drive_to_dist(target_dist_mm):
    targetDistance = 35
    speed = 300
    time_in_range = 0

    # Drive up to the obstacle
    while True:
        speed = (sensorUltraSonic.value() - target_dist_mm) * 2.5
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
    motorDriveLeft.stop(stop_action = "hold")
    motorDriveRight.stop(stop_action = "hold")


def look_for_ball():
    drive_to_dist(40)

    motorDriveLeft.run_timed(time_sp=500, speed_sp = 100)
    motorDriveRight.run_timed(time_sp=500, speed_sp = 100)

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = -100, speed_sp = 100)
    motorDriveRight.run_to_rel_pos(position_sp = -100, speed_sp = 100)

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = -236, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 236, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    drive_to_dist(40)

    motorDriveLeft.run_timed(time_sp=500, speed_sp = 100)
    motorDriveRight.run_timed(time_sp=500, speed_sp = 100)

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = -100, speed_sp = 100)
    motorDriveRight.run_to_rel_pos(position_sp = -100, speed_sp = 100)

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = 225, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = -225, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    # LOOK FOR IR BALL
    if(sensorIR.value()!=0):
        return
    sleep(1)

    motorDriveLeft.run_to_rel_pos(position_sp = 50, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 50, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = 225, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = -225, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    drive_to_dist(40)

    motorDriveLeft.run_to_rel_pos(position_sp = -100, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = -100, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = -236, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 236, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    # LOOK FOR IR BALL
    if(sensorIR.value()!=0):
        return
    sleep(1)

    motorDriveLeft.run_to_rel_pos(position_sp = -100, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = -100, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = -230, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 230, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    drive_to_dist(300)

    motorDriveLeft.run_to_rel_pos(position_sp = 230, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = -230, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = 300, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 300, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = 115, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = -115, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    motorDriveLeft.run_to_rel_pos(position_sp = 300, speed_sp = 150, stop_action = "hold")
    motorDriveRight.run_to_rel_pos(position_sp = 300, speed_sp = 150, stop_action = "hold")

    motorDriveLeft.wait_while('running')
    motorDriveRight.wait_while('running')

    # LOOK FOR IR BALL
    if(sensorIR.value()!=0):
        return
    sleep(1)

look_for_ball()

motorDriveLeft.run_to_rel_pos(position_sp = 400, speed_sp = 150, stop_action = "hold")
motorDriveRight.run_to_rel_pos(position_sp = 400, speed_sp = 150, stop_action = "hold")

motorDriveLeft.wait_while('running')
motorDriveRight.wait_while('running')

Sound.beep()
