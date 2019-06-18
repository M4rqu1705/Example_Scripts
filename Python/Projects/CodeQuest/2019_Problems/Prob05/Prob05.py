#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

for i in lines:
    bricklist = i.split(" ")
    small = int(bricklist[0])
    large = int(bricklist[1]) 
    size = int(bricklist[2])

    if size % 5 <= small and size // 5 <= large:
        print("true")
    elif size <= small:
        print("true")
    else:
        print("false")


# --- Your code goes here ---
