#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import matplotlib.pyplot as plt
import numpy as np

def find_line(x1, y1, x2, y2):
    # y - y1 = m(x - x1)
    # → y = m*(x - x1) + y1
    # → y = m*x - m*x1 + y1

    # y = mx + b → m = ((y2 - y1) / (x2 - x1)) & b = (y1 - m*x1)

    # Cannot divide by zero
    if x1 == x2:
        m = 10 ** 200
    else:
        m = (y2 - y1) / (x2 - x1)

    b = y1 - m*x1

    return (m, b)

def flatten(l):
    output = []
    for el in l:
        output.extend(list(el))

    return output


def main():
    x1, y1 = (0,    0)
    x2, y2 = (0.2,  1)
    x3, y3 = (0.4,  0.1)
    x4, y4 = (0.6,  0.6)
    x5, y5 = (0.8,  0.3)
    x6, y6 = (1,    0.5)

    coefficients = [
        find_line(x1, y1, x2, y2),
        find_line(x2, y2, x3, y3),
        find_line(x3, y3, x4, y4),
        find_line(x4, y4, x5, y5),
        find_line(x5, y5, x6, y6),
    ]

    for coefficient in coefficients:
        print(f'Line: y = {coefficient[0]} * x + {coefficient[1]}')

    domain = [
            np.arange(x1, x2 + 0.01, 0.01),
            np.arange(x2, x3 + 0.01, 0.01),
            np.arange(x3, x4 + 0.01, 0.01),
            np.arange(x4, x5 + 0.01, 0.01),
            np.arange(x5, x6 + 0.01, 0.01),
            ]

    codomain = [coefficients[i][0] * dom + coefficients[i][1] for i, dom in enumerate(domain) ]

    x = np.array(flatten(domain))
    y = np.array(flatten(codomain))

    #  x = np.round(x, 6)
    #  y = np.round(y, 3)


    degree = 5
    y_hat_coeff = np.polyfit(x, y, degree)

    y_hat = y_hat_coeff[0] * x ** degree
    y_hat_str = f'{y_hat_coeff[0]} * x ** {degree}'

    for i in range(1, degree):
        y_hat += y_hat_coeff[i] * x ** (degree - i)
        y_hat_str += f' + {y_hat_coeff[i]} * x ** {(degree - i)}'

    print(y_hat_str)

    
    plt.plot(x, y)
    plt.plot(x, y_hat)

    plt.show()




if __name__ == "__main__":
    main()

