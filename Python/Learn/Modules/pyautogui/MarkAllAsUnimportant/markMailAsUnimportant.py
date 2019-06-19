#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui as pag
import os
from time import sleep

def main():
    countdownTime = 0
    supportedFileTypes = ['.png', '.jpeg', '.jpg']

    # Countdown that gives a small timer for the user to switch screens
    for i in range(countdownTime, 0, -1):
        print("Starting in {}".format(i), end="\r")
        sleep(1)
        print(" "*20, end="\r")

    # Prepare program. We will need to reference images and changing current
    # working directory is very important
    programPath = os.path.dirname(os.path.realpath(__file__))
    os.chdir(programPath + "\\images")

    # Use pyautogui to locate button icons on screen. Take images
    # from files in image directory
    matches = []

    for image in os.listdir():
        if os.path.isfile(image) and os.path.splitext(image)[1].lower() in supportedFileTypes:
            try:
                temp = pag.locateAllOnScreen(image, confidence=.95)
                matches.extend(list(temp))
            except:
                pass

    #  Click on the center of every match, only if there were matches, of course
    if len(matches) > 0:
        for buttonRectangle in matches:
            x, y = pag.center(buttonRectangle)
            pag.click(x, y, clicks=1, button='left')
        print("Clicked a total of {} buttons".format(len(matches)))
    else:
        # If there were no matches, notify it
        print("No buttons found on screen!")


if __name__ == "__main__":
    # Run program eternally, or until keyboard interrupt
    while True:
        main()
        sleep(1)
