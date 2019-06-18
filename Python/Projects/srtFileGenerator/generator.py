#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re

def parseTime(time):
    hour, minute, second, millisecond = 0,0,0,0

    for item in time.split(","):
        item.lower().strip()
        if re.match(r'^[\S\s]+ms$', item):
            millisecond = int(item[:-2])
        elif re.match(r'^[\S\s]+s$', item):
            second = int(item[:-1])
        elif re.match(r'^[\S\s]+m$', item):
            minute = int(item[:-1])
        elif re.match(r'^[\S\s]+h$', item):
            hour = int(item[:-1])

    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    second = str(second).zfill(2)
    millisecond = str(millisecond).zfill(3)
            
    return (hour, minute, second, millisecond)


def main():

    # Enter filename with specific criteria
    filename = "*.str"
    while re.match(r'^[\S\s]*\.\w{1,4}$', filename):
        filename = input("Enter file name: ")
        filename = filename.strip()
    print()

    # Create relative path accordingly
    relPath = './output/{}.srt'.format(filename)

    # Prepare variables
    data = []

    # Check if we can open file
    if os.path.exists(relPath):
        with open(relPath, "r") as srtFile:
            fileData = srtFile.readlines()
            for index in range(len(fileData)):
                fileData[index] = fileData[index].strip() + "\n"
            fileData = ''.join(fileData)
            data = fileData.split('\n\n')
    else:
        prompt = "[×] File doesn't exist. \nCreate file by name of '{}.srt'? ".format(filename)
        createFile = str(input(prompt))

        if re.match(r'(?:ye?s?|si?)', createFile):
            with open(relPath, "w+") as srtFile:
                srtFile.writelines([""])
        else:
            exit()

    counter = 0
    if len(data) > 0:       
        # Update counter to take into account previous entry numbers
        counter = int(data[-1].strip().split('\n')[0]) + 1

    try:

        while True:
            # Retrieve entry start time
            startTime = input("[<<] Start time: ")
            temp = parseTime(startTime)
            startTime = "{}:{}:{}.{}".format(temp[0], temp[1], temp[2], temp[3])

            # Retrieve entry end time
            endTime = input("[<<] End time: ")
            temp = parseTime(endTime)
            endTime = "{}:{}:{}.{}".format(temp[0], temp[1], temp[2], temp[3])

            # Retrieve entry subtitle
            subtitles = input("[<<] Enter subtitle: ")
            subtitles = subtitles.strip()

            # Format output
            output = "{}\n{} --> {}\n{}\n".format(counter, startTime, endTime, subtitles)

            # Add output to data
            data.append(output)
            print()

            # Increase counter to keep track of entries 
            counter+=1

    except KeyboardInterrupt:
        with open(relPath, "w+") as srtFile:
            srtFile.writelines('\n\n'.join(data))
        print("Exiting program. Content was saved to {}".format(relPath)) 


if __name__ == "__main__":
    message = """

    Welcome to srt file generator!
Just enter the time and message of the subtitle, and you'll be done in no-time!

The time format must meet the following criteria:
    (1) Must use comma-separated values
    (2) Numbers must be followed by time unit, be it 'ms', 's', 'm' or 'h'

    """
    print(message)
    main()

