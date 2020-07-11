import matplotlib.pyplot as plt
import numpy as np
import math

def V(h):
    return math.pi * h**2 * (3*R - h) / 3


R = 3

H = np.linspace(0, 10, 100)
X = V(H)

fig, ax = plt.subplots()
ax.set_xlim(-10, 120)
ax.set_ylim(0, 10)
ax.set_title("Nivel de Agua (m) vs Volumen (m³)")
ax.set_xlabel("Volumen de agua (m³)")
ax.set_ylabel("Nivel de agua (m)")

ax.plot(X, H, 'tab:red')

plt.show()
