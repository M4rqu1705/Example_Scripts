#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("Prob05.in.txt") as f:
    read_data = f.readlines()
    T = int(read_data.pop(0))
    for i in range(T*2,2):
        last_year = read_data[i].split(",")
        print(last_year)
