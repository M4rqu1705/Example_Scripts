#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Thank you https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
# and thank you https://nerdparadise.com/programming/pygame/part1

from os import environ, chdir, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from time import sleep, time
from pyautogui import hotkey, typewrite, locateOnScreen, center, click

def playSound(soundFile):
    mixer.music.load(soundFile)
    mixer.music.play()

def openCodeRadio():
    # Open Google Chrome with Freecodecamp radio
    hotkey('win', 'r')
    typewrite("chrome https://coderadio.freecodecamp.org\r\n")
    sleep(1.5)

    # Locate play button and click
    try:
        location = locateOnScreen('playButton.png', grayscale=True, region=(1440, 810, 480, 270))
        x, y = center(location)
        click(x, y, clicks=1, button='left')
    except:
        print("Could not play CodeRadio automatically!")

def main():

    openCodeRadio()

    # Initialize sound mixer
    mixer.init()

    # Variables with sources of sound files
    chdir(path.dirname(path.realpath(__file__)))
    rest_tone = path.join("sounds", "rest.mp3")
    work_tone = path.join("sounds", "work.mp3")

    # Program execution variables for later use
    stop = False
    iterations = 1
    work_time, rest_time = 25*60, 5*60
    init_time = time()
    current_time = time()

    try:
        # Try to eternally loop through work and rest sound files
        while not stop:
            # Work phase
            playSound(work_tone)
            current_time = time()-init_time

            while(current_time < work_time):
                current_time = time()-init_time
                minutes = current_time//60
                seconds = int(current_time - minutes*60)

                message = "Work timer {}: {:02n}:{:02n}".format(iterations, minutes, seconds)
                print(message.strip(), end='\r')
                sleep(1)
            init_time = time()

            # Rest phase
            playSound(rest_tone)
            current_time = time()-init_time

            while(current_time < rest_time):
                current_time = time()-init_time
                minutes = current_time//60
                seconds = int(current_time - minutes*60)

                message = "Rest timer {}: {:02n}:{:02n}".format(iterations, minutes, seconds)
                print(message.strip(), end='\r')
                sleep(1)

            iterations += 1
            init_time = time()

    except KeyboardInterrupt:
        print("\nGoodbye! Hope you were productive!!")
        mixer.quit()
        exit(0)

if __name__ == "__main__":
    main()
