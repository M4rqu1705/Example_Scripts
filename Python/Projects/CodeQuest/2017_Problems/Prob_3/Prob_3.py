#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('Prob03.in.txt') as f:
    read_data = f.readlines()
    T = read_data.pop(0)
    for line in read_data:
        (num1, num2) = line.split(' ')
        print("%d %d" % (int(num1) + int(num2), int(num1) * int(num2)))
