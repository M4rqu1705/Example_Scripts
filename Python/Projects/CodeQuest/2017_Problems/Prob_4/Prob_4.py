#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fib(x):
    num1 = 1
    num2 = 0
    tmp = 0

    for i in range(x - 1):
        tmp = num1 + num2
        num2, num1 = num1, tmp

    return(num2)

with open('Prob04.in.txt') as f:
    read_data = f.readlines()
    T = read_data.pop(0)

    for i in read_data:
        print("%d = %d" % (int(i), fib(int(i))))

