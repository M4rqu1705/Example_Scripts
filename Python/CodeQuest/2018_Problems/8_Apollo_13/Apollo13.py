#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("Prob08.in.txt") as f:
    read_data = f.readlines()
    T = read_data.pop(0)

    for line in read_data:
        results = []
        for coordinates in line.split(' '):
            substraction = float(coordinates.strip()) - 180
            if substraction > 0:
                results.append(substraction)
            elif substraction >= 360:
                results.append(720 - substraction)
            elif substraction < 0:
                results.append(360 + substraction) 

        print("{:3.2f} {:3.2f} {:3.2f}".format(results[0], results[1], results[2])) 
