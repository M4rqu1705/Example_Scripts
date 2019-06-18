#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("Prob02.in.txt") as f:
    read_data = f.readlines()
    T = read_data.pop(0)

    for line in read_data:
        word, number = line.split(' ')
        word_list = []
        for char in word:
            word_list.append(char)
        word_list.pop(int(number))
        word = ''.join(word_list)
        print(word)



