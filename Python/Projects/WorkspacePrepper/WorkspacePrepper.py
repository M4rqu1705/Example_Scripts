#!/usr/bin/env python
# -*- coding: utf-8 -*-
from json import load
from os import chdir, listdir
from os.path import dirname, isfile, splitext
from re import search
from sys import argv
from time import sleep
import pyautogui

def getWorkspace():
    # Prepare list of workspaces available inside workspaces directory
    workspaces_available = listdir()
    # Prepare a list of numbers which will be matched to each workspace
    workspaces_indices = [index + 1 for index in range(len(workspaces_available))]
    # "Join" the two lists in order to assign each workspace a number 
    workspaces = dict(zip(workspaces_indices, workspaces_available))

    print("Please select which workspace file would you like to use.")
    for key, value in workspaces.items():
        print("({}) {}".format(key, value))

    _input = int(input("[<<] "))
    selectedWorkspace = workspaces[_input]

    return selectedWorkspace 

def inspectFile(data): 
    conditions = []
    error_message = 0
    format_message = "\nPlease make sure json with procedure follows following format:\n" + \
            "[\n" + \
            "   {\"operation\":[parameters]},\n" + \
            "   {\"operation\":[parameters]},\n" + \
            "   ...\n" + \
            "]\n"

    try:
        # Data must be a list
        conditions.append( bool(type(data) == list) )
        # Every element of the list must be a dictionary 
        conditions.append( bool(all([type(task) == dict for task in data])) )
        # Each task must only have one key indicating operation 
        conditions.append( bool(all([len(task.keys()) == 1 for task in data])) )
    except:
        # If any error occurs, the data is highly probable to not contain the
        # specified format
        conditions.append(False)
        error_message = format_message
    if all(conditions):
        return "File passed"
    else:
        # Make sure error_message was not previously defined 
        if error_message == 0:
            error_message = ""
            if not conditions[0]:
                error_message += "File is not a list!\n"
            if not conditions[1]:
                error_message += "List does not contain dictionaries with operations!\n"
            if not conditions[2]:
                error_message += "There is more than one operation in a task!\n"
            
            error_message += format_message
        print(error_message)
        exit()

def interpretFile(procedure):
    for task in procedure:
        # Extract first operation ...
        operation = list(task.keys())[0]
        # And its parameters
        data = task[operation]

        # Decide what operation is referred to and execute it
        if search(r'windowsRun|run', operation):
            # Normalize data before operating on it
            command = ' '.join(data).strip() + " \n"
            # Open Windows `run` menu
            pyautogui.hotkey('win', 'r')
            # Type in requested command
            pyautogui.typewrite(command)
            # Report back
            print("Executed '{}'".format(command.strip()))

        elif search(r'hotkeys?', operation):
            # Check https://pyautogui.readthedocs.io/en/latest/keyboard.html?highlight=typewrite#keyboard-keys
            # for reference
            # Normalize data before operating on it
            keys = [piece.strip() for piece in data]
            # Execute hotkey
            pyautogui.hotkey(*keys)
            # Report back
            print("Executed '{}' hotkey".format(', '.join(keys)))

        elif search(r'type|write', operation):
            # Normalize data before operating on it
            text = ' '.join(data)
            # Type in requested text
            pyautogui.typewrite(text)
            # Report back
            print("Wrote '{}'".format(text))

        elif search(r'sleep|wait', operation):
            # Normalize data before operating on it
            sleep_time = float(sum(data))
            # Sleep for calculated amount of time
            sleep(sleep_time)
            # Report back
            print("Waited {} seconds".format(sleep_time))

        else:
            print("IDK what to do")


def main():
    # Make sure to remove script name from system arguments
    script_name = argv.pop(0)
    # Just to be sure, change to the workspaces' directory
    workspaces_path = ""
    try:
        workspaces_path = dirname(script_name) + '\workspaces'
        chdir(workspaces_path)
    except:
        workspaces_path = dirname(script_name) + 'workspaces'
        chdir(workspaces_path)

    # Prepare parameters variable
    parameters = argv

    # If parameters is empty, request the user to specify workspace
    if len(parameters) == 0:
        parameters = [getWorkspace()]

    # Loop through each file indicated by parameter and interpret them
    for parameter in parameters:

        # Parameter MUST BE a JSON file, so this line is a little redundant when
        # format is corrent, but we want to be safe
        parameter = splitext(parameter)[0] + ".json"
        # Extract data file indicated by parameter
        procedure = ""
        if isfile(parameter): # Only try to read parameter if it is a file
            with open(parameter, 'r') as f:
                procedure = load(f)
        else:
            print("{} skipped since it is not a file".format(parameter))
            continue

        # Make sure file fulfills minimal criteria
        print(inspectFile(procedure))

        interpretFile(procedure)



if __name__ == "__main__":
    main()

