#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    q = int(sys.stdin.readline().strip())
    lines.append(q)
    for d in range(q):
        lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

for i in range(T):
    repeat = int(lines.pop(0))
    numbers = []
    for c in range(repeat):
        numbers.append(float(lines.pop(0).strip()))

    outputs = []
    for number in numbers:
        temp = (number - min(numbers)) / (max(numbers) - min(numbers)) * 255
        outputs.append(str(round(temp)))

    print("\n".join(outputs))


# --- Your code goes here ---
