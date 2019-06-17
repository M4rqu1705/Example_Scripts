#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import curses
import re


def setBackground(screen, height, width, mode="default"):
    """ Set up application's standard background.

        Parameters
        screen: (curses screen object) Screen to which to add the background
        height: (int) Screen's height
        width: (int) Screen's width

        Return: 
        Does not return anything

       ┌───────────────────────────────────────────────────────────────────────┐
       │ [<<]                                                                  │
       ╞═════════════════════════════════════════════════════════════════[mode]╡
       │                                                                       │
       │                                                                       │
       │                                                                       │
       └───────────────────────────────────────────────────────────────────────┘
    """

    contentWidth = width - 4
    mode = "[{}]".format(mode)

    contents = [
            "┌{}┐".format("─" * contentWidth),
            "│[<<]{}│".format(" " * (contentWidth-4)),
            "╞{}{}╡".format("═" * (contentWidth-len(mode)), mode),
            "│{}│".format(" " * contentWidth),
            "└{}┘".format("─" * contentWidth)
            ]

    screen.addstr(0, 0, contents[0])
    screen.addstr(1, 0, contents[1])
    screen.addstr(2, 0, contents[2])
    for line in range(3, height-1):
        screen.addstr(line, 0, contents[3])
    screen.addstr(height-1, 0, contents[4])


def controlUserInput(text, cursor, key, width):
    """ Manipulates text and updates it according to key and cursor

        Parameters
        text: (str) Text to manipulate
        cursor: (int) Cursor position inside `text`
        key: (int) Key to be interpreted
        width: (int) Width 

        Return
        Tuple of updated text and cursor position

    """

    if(key == curses.KEY_LEFT):              # Left arrow
        cursor -= 1 if cursor > 0 else 0

    elif(key == 443):                        # Ctrl + Left arrow
        wordBounds = [' ', '.', '_']
        offset = 2
        scanIndex = cursor - offset

        while(0 <= scanIndex and text[scanIndex] not in wordBounds):
            offset += 1
            scanIndex = cursor - offset

        cursor += -offset + 1
        cursor = cursor if 0 < cursor else 0

    elif(key == curses.KEY_RIGHT):           # Right arrow
        cursor += 1 if cursor < len(text) else 0

    elif(key == 444):                        # Ctrl + Right arrow
        wordBounds = [' ', '.', '_']
        offset = 2
        scanIndex = cursor + offset

        while(scanIndex < len(text) and text[scanIndex] not in wordBounds):
            offset += 1
            scanIndex = cursor + offset

        cursor += offset + 1
        cursor = cursor if cursor < len(text) else len(text)-1

    elif(key == 262):                        # Home key
        cursor = 0

    elif(key == 358):                        # End key
        cursor = len(text)-1

    elif(key == 330):                        # Delete
        if cursor < len(text):
            removeChar = lambda string, pos: string[:pos] + string[pos+1:]
            text = removeChar(text, cursor)

    elif(key == 8):                          # Backspace
        if cursor > 0:
            removeChar = lambda string, pos: string[:pos] + string[pos+1:]
            text = removeChar(text, cursor-1)
            cursor -= 1

    elif(key == 21):                        # Ctrl + U
        cursor = 0
        text = ""

    #  elif key in [10, 13]:                # \n or \r
        #  if text.strip().lower() in ["exit", "quit"]:
            #  break

    elif(re.match(r'(?:\w|\d|\t| )', str(chr(key)))):    # Alphanumeric or \t and spaces
        if(len(text) < width-1):
            insertChar = lambda char, string, pos: string[:pos] + char + string[pos:]
            text = insertChar(chr(key), text, cursor)
            cursor += 1 if cursor < width else 0

    return(text, cursor)


def main(stdscr):

    curses.noecho()
    curses.curs_set(2)

    userInput = ""
    key = 8
    textboxInit = (1, 6)
    cursorPos = 0
    height, width = stdscr.getmaxyx()
    mode = "es-def"


    while 1:
        stdscr.clear()          # Clear screen

        setBackground(stdscr, height, width, mode)

        # Update userInput and cursorPos
        userInput, cursorPos = controlUserInput(userInput, cursorPos, key, (width-9))

        if userInput in ["exit", "quit"]:
            break
        else:
            mode = userInput.strip().lower()

        # Add user input
        stdscr.addstr(textboxInit[0], textboxInit[1], userInput)
        # Make a cursor
        stdscr.chgat(textboxInit[0], textboxInit[1] + cursorPos, 1, curses.A_STANDOUT)

        stdscr.refresh()
        key = stdscr.getch()    # Stop program and wait to receive a character 

if __name__ == "__main__":
    curses.wrapper(main)
