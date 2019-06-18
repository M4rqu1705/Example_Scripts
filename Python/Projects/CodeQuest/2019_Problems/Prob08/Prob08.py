#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

for line in lines:
    grid = [[10]*20]*20

    row, column = line.split(" ")
    row = int(row)
    column = int(column)
    _100pos = (row, column)

    _50pos = []
    for c in range(-1, 2, 1):
        if not (0 <= row+c < 20):
            break
        for d in range(-1, 2, 1):
            if 0 <= column+d < 20:
                _50pos.append(tuple([row+c, column+d]))

    _25pos = []
    for c in range(-2, 3, 1):
        if not (0 <= row+c < 20):
            break
        for d in range(-2, 3, 1):
            if 0 <= column+d < 20:
                _25pos.append(tuple([row+c, column+d]))

    #  print("'{}', '{}'".format(_100pos[0], _100pos[1]))

        
    for coords in _25pos:
        grid[coords[0]][coords[1]] = 25

    for coords in _50pos:
        grid[coords[0]][coords[1]] = 50

    grid[_100pos[0]][_100pos[1]] = 100

    for c in grid:
        for d in c:
            print(d, end=',')
        print()



# --- Your code goes here ---
