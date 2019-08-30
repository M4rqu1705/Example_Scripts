#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Thank you https://stackoverflow.com/questions/7746263/how-can-i-play-an-mp3-with-pygame
# and thank you https://nerdparadise.com/programming/pygame/part1
import pygame
import time

def main():
    pygame.init()

    paused = False
    stop = False
    relax_tone = "sounds\\relax.mp3"
    work_tone = "sounds\\work.mp3"
    pygame.init()
    pygame.mixer.init()


    try:
        while not stop:
            pygame.mixer.music.load(relax_tone)
            pygame.mixer.music.play()
            pygame.event.wait()
            sleep(25 * 60)
            pygame.mixer.music.load(work_tone)
            pygame.mixer.music.play()
            pygame.event.wait()
            sleep(5 * 60)

    except KeyboardInterrupt:
        print("Goodbye!")



if __name__ == "__main__":
    main()

