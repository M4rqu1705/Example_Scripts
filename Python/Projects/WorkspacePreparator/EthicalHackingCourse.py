#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyautogui
from time import sleep

def windowsRunMenu(command):
    # Open Windows `run` menu 
    pyautogui.hotkey('win', 'r')
    # Type in requested command
    command = command.strip() + " \n"
    pyautogui.typewrite(command)


def main():
    # Open udemy.com on the Ethical Hacking course 
    windowsRunMenu('chrome https://www.udemy.com/penetration-testing/learn/lecture/2605392 ')

    # Open Vim with the markdown file
    windowsRunMenu('vim "C:\\Users\\m4rc0\\Documents\\The\ Complete\ Ethical\ Hacking\ Course.md" ')

    # Open Ubuntu to find command's help files
    windowsRunMenu('ubuntu')


if __name__ == "__main__":
    main()

