import matplotlib.pyplot as plt
import numpy as np
import math

def f(h):
    return math.pi * h**3 - 3 * math.pi * R * h**2 + 3 * V


V = 30
R = 3

X = np.linspace(-10, 10, 100)
Y = f(X)

fig, ax = plt.subplots()
ax.set_xlim(-4, 10)
ax.set_ylim(-255, 100)
ax.set_title("Volumen que falta llenar vs Nivel de agua")
ax.set_xlabel("Nivel de agua (m)")
ax.set_ylabel("Volumen falta llenar (m³)")

ax.plot(X, Y, 'tab:red')

plt.show()
