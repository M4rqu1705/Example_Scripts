#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---
for i in lines:
    glist = i.split(" ")
    if glist[0] == "true":
        g1 = True
    elif  glist[0] == "false":
        g1 = False 

    if glist[1] == "true":
        g2 = True
    elif  glist[1] == "false":
        g2 = False 

    if g1 == g2:
        print("true")
    else:
        print("false")

# --- Your code goes here ---
