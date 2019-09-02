#!/usr/bin/python
from time import sleep
from winsound import Beep
import re

#Regular expression to be used to classify the input number between minutes and seconds
unitClassifier = re.compile('\d+\s(min|mins|minute|minutes)')


def convertUnits(string):
    ''' If necessary multiply numerical unput by 60 to convert from secons to minutes'''
    
    output, string = 0, string.lower().strip()

    if unitClassifier.search(string):  #If any of the strings in the regular expression are found
        output = int(float(re.compile('(\d*\.\d+|\d+)').match(string).group(1)) * 60.0)  #Multiply the retrieved number, be it integer or boolean, by 60 and store it as an integer
    else:
      output = int(re.compile('(\d+)').match(string).group(1)) #Retrieve the number as it is and store it as an integer

    return output


#Preset variables to 0
time1, time2 = 0, 0

print("[*] Welcome to the Pomodoro timer!\n[*] In the following prompts, enter the amount of MINUTES or SECONDS you will work\n")

_in = input("[*] Enter how much time you will work in:\n\t>>> ")
time1 = convertUnits(_in)

_in = input("[*] Enter how much time you will rest for:\n\t>>> ")
time2 = convertUnits(_in)

iterations = int(input("[*] Enter how many Pomodoros you would like to do:\n\t>>> "))


for number in range(1, iterations+1):
  print(str(number) + " pomodoro begun")
  sleep(time1)
  for c in range(4):
      Beep(1500, 400)
  print(str(number) + " rest begun")
  sleep(time2)
  for c in range(4):
      Beep(1000, 400)
  print(str(number) + " pomodoro ended")
