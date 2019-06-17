#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

lines = []

for c in range(T):
    for d in range(2):
        lines.append(sys.stdin.readline().strip())

# --- Your code goes here ---

def decode(shift, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for c in message:
        if alphabet.count(c) > 0:
            d = alphabet[alphabet.index(c) - shift % (len(alphabet))]
            result += d
        else:
            result += c
    return result

for i in range(T):
    shift = int(lines.pop(0))
    message = str(lines.pop(0).strip())

    print(decode(shift,message))
# --- Your code goes here ---
