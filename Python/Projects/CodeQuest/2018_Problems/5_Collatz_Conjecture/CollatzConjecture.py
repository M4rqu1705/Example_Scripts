#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Docstring goes here
'''

__author__ = 'Marcos R. Pesante Colón'
__email__ = 'm4rc05.dev@gmail.com'
__date__ = ''
__license__ = 'GNU GPL V.3'
__version__ = '1.0'

def collatz(num, length):
    if num != 1:
        if num%2 == 0:
            num *= 0.5
        else:
            num = num*3 + 1

        length+=1

        return (collatz(num,length))
    return length

def main():

    numbers = []
    with open("Prob05.in.txt") as f:
        read_data = f.readlines()
        T = read_data.pop(0)
        numbers = [int(x.strip()) for x in read_data]
         
    for number in numbers:
        print("{}:{}".format(number, collatz(number, 1)))



if __name__ == '__main__':
    main()
