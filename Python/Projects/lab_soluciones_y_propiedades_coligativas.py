# -*- coding: utf-8 -*-
"""Lab Soluciones y Propiedades Coligativas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UUBWSQhw1zHvIHWcI4vsnELqzCPeTPNi
"""

import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Tiempos de 0 a 300 en intervalos de 15
time = list(range(0, 301, 15))

data = [
    # Parte 1, Temperaturas 1
    [27, 26, 18, 13, 10, 8, 7, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5],
    # Parte 1, Temperaturas 2
    [20, 18, 15, 12, 10, 9, 8, 7, 7, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4],
    # Parte 2, Temperatura 1
    [27, 23, 15, 10, 7, 6, 5, 4, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1],
    # Parte 2, Temperatura 2
    [25, 7, 3, 3, 3, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
]

# Preparar estructuras para almacenar funciones y coeficientes
# a, b, c = 0, 0, 0
coefficients = [[0, 0, 0] for x in range(len(data))]

f = lambda x, a, b, c: a*b**x + c
f_prime = lambda x, a, b: a*b**x*np.log(b)

# Realizar regresión
for i, datum in enumerate(data):
    popt, pcov = curve_fit(f, time, datum)
    coefficients[i] = popt

functions = [
    lambda x: f(x, *coefficients[0]),
    lambda x: f(x, *coefficients[1]),
    lambda x: f(x, *coefficients[2]),
    lambda x: f(x, *coefficients[3]),
]

derivatives = [
    lambda x: f_prime(x, *(coefficients[0][:2])),
    lambda x: f_prime(x, *(coefficients[1][:2])),
    lambda x: f_prime(x, *(coefficients[2][:2])),
    lambda x: f_prime(x, *(coefficients[3][:2])),        
]
tangents = [
    lambda x, x0: derivatives[0](x0)*(x - x0) + functions[0](x0),
    lambda x, x0: derivatives[1](x0)*(x - x0) + functions[1](x0),
    lambda x, x0: derivatives[2](x0)*(x - x0) + functions[2](x0),
    lambda x, x0: derivatives[3](x0)*(x - x0) + functions[3](x0),
]

num_plots = 4
#  # Graficar datos para corroborar regresiones
#  fig, axes = plt.subplots(num_plots)
#  fig.set_size_inches(10.5, num_plots*10)

#  if not isinstance(axes, np.ndarray):
    #  axes = [axes]

#  for i in range(num_plots):
    #  axes[i].plot(time, data[i], label='Datos Experimentales')
    #  axes[i].plot(time, [functions[i](t) for t in time], label='Regresión Exponencial')
    #  axes[i].set_title('Temperatura de Ciclohexano versus tiempo')
    #  axes[i].set_xlabel('tiempo (s)')
    #  axes[i].set_ylabel('Temperatura (°C)')
    #  axes[i].legend()

#  plt.show()

x0 = [15, 15, 15, 15]
x1 = [170, 170, 170, 60]

fig, axes = plt.subplots(num_plots)
fig.set_size_inches(10.5, num_plots*10)

if not isinstance(axes, np.ndarray):
    axes = [axes]

for i in range(len(data)):
    # Graficar curvas y tangentes
    axes[i].plot(time, data[i], label='Datos Experimentales')
    axes[i].plot(time, [functions[i](t) for t in time], label='Regresión Exponencial')
    axes[i].plot(time, [tangents[i](t, x0[i]) for t in time], label='Tangente 1')
    axes[i].plot(time, [tangents[i](t, x1[i]) for t in time], label='Tangente 2')
    axes[i].set_ylim(bottom=0)
    axes[i].set_xlim(left=-15)

    # Calcular dónde se encuentran las tangentes
    x_intersection = (derivatives[i](x0[i])*x0[i] - derivatives[i](x1[i])*x1[i] + functions[i](x1[i]) - functions[i](x0[i])) / (derivatives[i](x0[i]) - derivatives[i](x1[i]))
    y_intersection = tangents[i](x_intersection, x0[i])
    print(f'Punto de congelación experimental Parte {i//2+1}, Prueba {i%2+1}: {round(y_intersection, 2)}°C')

    # Identificar punto de intersección
    axes[i].hlines(y_intersection, -15, x_intersection, linestyles='--', label='Temperatura de Fusión Experimental')

    # Etiquetar con títulos y nombres de ejes
    axes[i].set_title(f'Temperatura de Ciclohexano versus tiempo (Parte {i//2+1}, Prueba {i%2+1})')
    axes[i].set_xlabel('tiempo (s)')
    axes[i].set_ylabel('Temperatura (°C)')
    axes[i].legend()

plt.show()