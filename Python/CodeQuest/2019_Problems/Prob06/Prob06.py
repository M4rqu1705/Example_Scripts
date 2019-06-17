#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

for line in lines:
    height = int(line)
    pi = 3.141592653
    earthCircumference = 40075

    output = round(earthCircumference + 2 * pi * height, 1)
    print(output)


# --- Your code goes here ---
