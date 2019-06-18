#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('Prob05.in.txt') as f:
    read_data = f.readlines()
    T = int(read_data.pop(0))

    for i in range(0, len(read_data), 2):

        last_year = read_data[i].strip().split(',')
        current_year = read_data[i+1].strip().split(',')
        both = []

        for c in last_year:
            for d in current_year:
                if c == d:
                    both.append(c)

        for person in both:
            current_year.remove(person)
            last_year.remove(person)

        both.sort()
        current_year.sort()
        last_year.sort()

        print(','.join(last_year))
        print(','.join(both))
        print(','.join(current_year))

