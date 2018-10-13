#!/usr/bin/python
from time import sleep
from winsound import Beep

speed = float(input("What speed should the music play at: "))

times = [float(0.25/speed), float(1/speed), float(1.2/speed)]

while True:
    sleep(times[0])
    Beep(500, 100)
    sleep(times[0])
    Beep(500, 100)
    sleep(times[1])
    Beep(500, 100)
    sleep(times[2])

