#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses

def main(stdscreen):
    # Your code starts here ---------------------------------------------------

    key = stdscreen.getch()
    print("Key = '{}'".format(key))

    # Your code ends here -----------------------------------------------------


if __name__ == "__main__":
    curses.wrapper(main)

