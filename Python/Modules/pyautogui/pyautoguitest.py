#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import cos, sin
from time import sleep, time
import pyautogui as pygui

def main():
    # Your code starts here ---------------------------------------------------

    sleep(2)

    try:
        #  theta = 0
        #  r = 1
        #  pygui.moveTo(960, 512)

        #  while r < 100:
            #  x = r * cos(theta)
            #  y = r * sin(theta)

            #  pygui.dragTo(960 + x, 512 + y)

            #  r+=0.1
            #  theta += 0.1

        distance = 100
        reduction = 1.5
        pygui.moveTo(560, 512)
        while distance > 0:
            pygui.dragRel(distance, 0)
            distance -= reduction
            pygui.dragRel(0, -distance)
            distance -= reduction
            pygui.dragRel(-distance, 0)
            distance -= reduction
            pygui.dragRel(0, distance)
            distance -= reduction


        distance = 100
        reduction = 1
        pygui.moveTo(680, 512)
        while distance > 0:
            pygui.dragRel(distance, 0)
            distance -= reduction
            pygui.dragRel(0, -distance)
            distance -= reduction
            pygui.dragRel(-distance, 0)
            distance -= reduction
            pygui.dragRel(0, distance)
            distance -= reduction

        distance = 100
        reduction = 0.75
        pygui.moveTo(800, 512)
        while distance > 0:
            pygui.dragRel(distance, 0)
            distance -= reduction
            pygui.dragRel(0, -distance)
            distance -= reduction
            pygui.dragRel(-distance, 0)
            distance -= reduction
            pygui.dragRel(0, distance)
            distance -= reduction

    except KeyboardInterrupt:
        print("Goodbye!")


        # Your code ends here -----------------------------------------------------


if __name__ == "__main__":
    main()

