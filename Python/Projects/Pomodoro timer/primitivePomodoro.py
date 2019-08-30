#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thank you https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
# and thank you https://nerdparadise.com/programming/pygame/part1
from os import environ, chdir, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer
from time import sleep, time

def playSound(soundFile, seconds):
    mixer.music.load(soundFile)
    mixer.music.play()
    sleep(seconds)


def main():
    # Initialize sound mixer
    mixer.init()

    # Variables with sources of sound files
    chdir(path.dirname(path.realpath(__file__)))
    rest_tone = path.join("sounds", "rest.mp3")
    work_tone = path.join("sounds", "work.mp3")

    # Program execution variables for later use
    paused = False
    stop = False
    init_time = time()
    current_time = 0

    try:
        # Try to eternally loop through work and rest sound files
        while not stop:
            #  playSound(work_tone, 25 * 60)
            #  current_time = time() - init_time
            #  while(current_time < 25 * 60):
                #  current_time = time() - init_time
                #  print(int(current_time), end="\r")
            #  playSound(rest_tone, 5 * 60)
            #  current_time = time() - init_time
            #  while(current_time < 5 * 60):
                #  current_time = time() - init_time
                #  print(int(current_time), end="\r")
            #  init_time = time()
            playSound(work_tone, 25 * 60)
            playSound(rest_tone, 5 * 60)

    except KeyboardInterrupt:
        print("Goodbye!")
        mixer.quit()


if __name__ == "__main__":
    main()
