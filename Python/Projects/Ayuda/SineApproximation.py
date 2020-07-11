#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def factorial(x):
    total = 1
    for i in range(x, 1, -1):
        total = total * i

    return total

def seno(x, terminos):
    total = x
    i = 3
    signo = "-"

    while i // 2 < terminos:

        if signo == "+":
            total = total + ((x ** i) / factorial(i))
            signo = "-"

        else:
            total = total - ((x ** i) / factorial(i))
            signo = "+"

        i = i + 2

    return total

def error_relativo(a, b):
    return abs((a - b) / ((a + b) / 2) * 100)



error_disponible = float(input("¿Cuál es el error relativo que está dispuesto a aceptar? "))
radianes = float(input("¿De qué valor quiere buscar su seno (en radianes)? "))

error_disponible = round(error_disponible, 4)
radianes = round(radianes, 4)

terminos = 1
real = np.sin(radianes)
aprox = seno(radianes, terminos)

while error_relativo(real, aprox) > error_disponible:
    terminos = terminos + 1
    aprox = seno(radianes, terminos)

print()
print("Para aproximar sin(" + str(round(radianes, 4)) + ") con un error relativo de " + str(round(error_relativo(real, aprox), 4)))
print(" necesitas " + str(terminos) + " terminos que resulta en una aproximación de " + str(round(aprox, 4)))
