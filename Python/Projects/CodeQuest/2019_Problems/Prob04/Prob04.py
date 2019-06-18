#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---
for i in lines: 
    speedlist = i.split(" ")
    speed = int(speedlist[0])
    
    if speedlist[1] == "true":
        speed -= 5

    if speed <= 60:
        print("no ticket")
    
    elif 61 <= speed <= 80:
        print("small ticket")
    
    else:
        print("big ticket")

# --- Your code goes here ---
