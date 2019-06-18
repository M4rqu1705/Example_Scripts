#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

with open("Prob07.in.txt") as f:
    read_data = f.readlines()
    T = read_data.pop(0)

    while len(read_data) > 0 and re.match(r'^\d+$', read_data[0].strip()):
        N = int(read_data.pop(0))

        not_palindromes = []
        for c in range(N):
            word = read_data.pop(0)
            word = word.lower().strip()

            if word[::-1] != word:
                not_palindromes.append(str(c+1))

        if len(not_palindromes) == 0:
            print("True")
        else:
            print("False - {}".format(", ".join(not_palindromes)))
