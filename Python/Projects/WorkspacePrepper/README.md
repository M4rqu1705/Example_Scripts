# Workspace Prepper
#### Prepare your workspace in an automated manner!

Sometimes I feel very motivated to do a specific task ... until I have to wait for the computer to turn on, wait for it to load, open each program independently, wait for them to load, and _then_ I can do what I initially wanted. However, I frequently face the problem of losing motivation and getting distracted while doing these tasks one by one. However, why not automate them? I don't frequently change tasks, and usually do the same thing one by one, so I have developed a small program to interface with the Windows 10 GUI in order to solve this problem

My script reads a specific json file with an ordered procedure that specifies what to do in order to set up my environment. By no means is this a safe script. It is very hackable, but I desgined it as a tool to help me, so I won't develop it with the object of distribution.

The json file format is the following:
```json
[
    {"operation" : [parameters]},
    {"operation" : [parameters]}
    ...
]
```
It is very important to note that the operation must have double quotes surrounding it and that the parameters are in fact a list. They can only hold a single, solitary number, but it MUST be a list, or else the programm will stop after showing a formatting error message.

The operations that my script supports to this day are:
* `windowsRun`: This operation opens a windows run menu and types in whatever you write and an <enter> to end your command(s)
    + If the parameter list has more than one command, the script will concatenate these separated by spaces.
* `hotkey`: This operation will execute a sequence of key presses similar to that of a hotkey, such as "alt", "tab", etc. 
    + Each key press must be an independent element of the parameter list
* `type`: This operation literally writes text to the screen as if were were typing it in a keyboard, but in a very quick manner.
    + If more than one parameter is given, script will concatenate these separated by spaces
* `write`: The same as `type`
* `sleep`: Halt procedure operation for a definite amount of time in seconds.
    + If the parameter list has more than one element, it will sum these elements in order to determine the amount of seconds to wait. 
* `wait`: The same as `sleep`

Hope it helps!
