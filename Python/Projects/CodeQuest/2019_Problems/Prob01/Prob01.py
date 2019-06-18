#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---
for i in lines: 
    i = i.lower()
    print(i)
# --- Your code goes here ---
