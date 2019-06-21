#!/usr/bin/env python
# -*- coding: utf-8 -*-
from json import load
from os import chdir
from os.path import dirname, isfile
from re import search
from sys import argv
from time import sleep
import pyautogui

def main():
    # Make sure to remove script name from system arguments
    script_name = argv.pop(0)
    # Just as a safety measure, change to this script's directory
    script_path = dirname(script_name)
    chdir(script_path)

    # Prepare parameters variable ...
    parameters = argv
    # Which we will loop through and interpret
    for parameter in parameters:
        parameter += ".json"
        # Extract data file indicated by parameter
        procedure = ""

        # Only try to read parameter if it is a file
        if isfile(parameter):
            with open(parameter, 'r') as f:
                procedure = load(f)

        # Make sure file fulfills minimal criteria, or else print and error and exit
        if type(procedure) != list or any([len(x.keys()) > 1 for x in procedure]):
            error_message = "Please make sure json with procedure follows following format:\n" + \
                "[\n" + \
                "   {\"operation\":[parameters]},\n" + \
                "   {\"operation\":[parameters]},\n" + \
                "   ...\n" + \
                "]\n"
            print(error_message)
            exit()

        # Interpret instructions
        for step in procedure:
            # Extract operation ...
            operation = list(step.keys())[0]
            # And its parameters
            data = step[operation]

            # Decide what to do and execute it
            if search(r'windowsRun', operation):
                command = ' '.join(data).strip() + " \n"
                # Open Windows `run` menu
                pyautogui.hotkey('win', 'r')
                # Type in requested command
                pyautogui.typewrite(command)
                # Report back
                print("Executed '{}'".format(command))
            elif search(r'hotkeys?', operation):
                # Check https://pyautogui.readthedocs.io/en/latest/keyboard.html?highlight=typewrite#keyboard-keys
                # for reference
                keys = [piece.strip() for piece in data]
                # Execute hotkey
                pyautogui.hotkey(*keys)
                # Report back
                print("Executed '{}' hotkey".format(', '.join(keys)))
            elif search(r'type|write', operation):
                text = ' '.join(data)
                # Type in requested text
                pyautogui.typewrite(text)
                # Report back
                print("Wrote '{}'".format(text))
            elif search(r'sleep|wait', operation):
                sleep_time = float(sum(data))
                # Sleep for calculated amount of time
                sleep(sleep_time)
                # Report back
                print("Waited {} seconds".format(sleep_time))
            else:
                print("IDK what to do")



if __name__ == "__main__":
    main()

