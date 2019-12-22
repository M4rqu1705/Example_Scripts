#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def simpson(f, a, b, n=10):
    dxi = (b-a)/n
    terms = f(np.linspace(a,b,n+1))
    terms[1:-1:2] *= 4
    terms[2:-2:2] *= 2
    return (dxi/3) * sum(terms)

def trapezoid(f, a, b, n=10):
    dxi = (b-a)/n
    terms = f(np.linspace(a,b,n+1))
    terms[1:-1] *= 2
    return (dxi/2) * sum(terms)

def motion_profile(x, a, h, l):
    if h<0:
        h = 2
    elif h%2!=0:
        h+=1

    return a*(1-np.cos(np.pi*x/l)**h)


def main():
    distance = 100
    max_speed = 83.775804
    average_speed = (1/distance) * simpson(lambda x: motion_profile(x, max_speed, 4, distance), 0, distance, 100)

    time = distance/average_speed

    print(f"Distance:{distance}, Time:{time}, Average Speed:{average_speed}")


if __name__ == "__main__":
    main()

