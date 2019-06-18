#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("Prob06.in.txt") as f:
    read_data = f.readlines()
    T = read_data.pop(0)
    for line in read_data:
        status = line.split(' ')
        numbers = []
        for counter in range(len(status)):
            numbers.append((status[counter].strip().lower() == "broken") * (2**(3-counter)))

        leds = []

        for c in range(4):
            for d in range(4):
                if (c*4) + d == sum(numbers):
                    leds = [c, d]
                
        colors = {0:"off", 1:"red", 2:"green", 3:'blue'}
        print("{} {}".format(colors[leds[0]], colors[leds[1]]))

