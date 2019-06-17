#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

def combination(x):
    results = ""
    if x == 0:
        return ""
    if x == 1:
        return "01"
    else:
        for i in combination(x-1):
            for j in combination(1):
                results += i + j
    return results

for line in lines:
    number = int(line.strip())

    ## ALL WE NEED TO DO IS PRINT THE NUMBERS THE WAY THEY WANT 😢
    for i in range(len(combination(number)),number):
        print(c)


        

# --- Your code goes here ---
