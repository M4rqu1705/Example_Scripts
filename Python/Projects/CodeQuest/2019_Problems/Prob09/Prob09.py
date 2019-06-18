#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

for line in lines:
    temp = line.replace(" ", ",")
    temp = temp.replace("and", ",")
    while temp.count(",,") > 0:
        temp = temp.replace(",,",",")

    hh, mm, ss = 0, 0, 0

    data = temp.split(",")

    for time in data:
        time = time.strip().lower()
        if time.endswith("h"):
            hh = int(time[0:-1])
        elif time.endswith("m"):
            mm = int(time[0:-1])
        elif time.endswith("s"):
            ss = int(time[0:-1])

    output = "{:02.0f}:{:02.0f}:{:02.0f}".format(hh, mm, ss)

    print(output)

# --- Your code goes here ---
