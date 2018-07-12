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

# Initialization
sensorLight.mode = "REFLECT"
sensorColor.mode = "COL-COLOR"
sensorUltraSonic.mode = "US-DIST-IN"
sensorIR.mode = "AC"

while True:
    lcd.clear()
    lcd.draw.text((48, 13), str(sensorIR.value()))
    lcd.update()
    sleep(1)
