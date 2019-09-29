#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui
from time import sleep

def main():
    # Your code starts here ---------------------------------------------------

    sleep(5)

    playButton = ".\Images\PlayAudio.png"
    startButton = ".\Images\StartRecording.png"


    try:
        playLocation = pyautogui.locateCenterOnScreen(playButton)
        startLocation = pyautogui.locateCenterOnScreen(startButton)

        pyautogui.click(playLocation.x, playLocation.y)
        pyautogui.click(startLocation.x, startLocation.y)
        for i in range(4):
            pyautogui.hotkey('win', 'down')
    except:
        print("Images not found on screen!")



    # Your code ends here -----------------------------------------------------


if __name__ == "__main__":
    main()

