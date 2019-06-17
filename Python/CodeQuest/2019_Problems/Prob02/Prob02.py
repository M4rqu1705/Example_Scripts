#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---
for i in lines:
    numlist = i.split(" ")

    num = int(numlist[0])
    num2 = int(numlist[1])

    if num == num2:
        result = num * 4
        print(str(result))

    else:
        result = num + num2
        print(str(result))

# --- Your code goes here ---
