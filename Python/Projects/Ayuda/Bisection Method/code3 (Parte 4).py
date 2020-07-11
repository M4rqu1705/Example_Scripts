import math
import matplotlib.pyplot as plt
import numpy as np

# Function f(h) for the gap between the desired volume V and the volume obtained with the current
# water level h given a sperical tank of radius R
def f(h):
    return math.pi * h**3 - 3 * math.pi * R * h**2 + 3 * V

def bisection_method(a0, b0, errorTolerance, maxIterations):
    a = a0
    b = b0

    # Initialize counter to track iterations
    iterations = 0

    # Use an error tolerance as stop criteria (Stop criteria #1) and max number of iterations (Stop
    # criteria #3)
    while abs(a - b) > errorTolerance and iterations < maxIterations:
        # Search for mid-point between a and b
        c = (a + b) / 2

        # If a and c change signs (hence their product is negative), crop right side
        if f(a) * f(c) < 0:
            b = c

        # Otherwise, b and c changed signs and the left side must be cropped
        else:
            a = c

        # Increase iterations counter by 1
        iterations += 1

    return c


# Input some program requirements
#  errorTolerance = eval(input("What is the maximum accepted error tolerance between a and b?: "))
errorTolerance = 1E-10

#  maxIterations = eval(input("What is the maximum amount of iterations accepted?: "))
maxIterations = 1E10

#  V = eval(input("How much volume do you want to hold? (meters³): "))
V = 30

#  R = eval(input("What is the sperical tank's radius? (meters): "))
R = 3


# There are a total of three roots. Using desmos.com/calculator for reference, these are:
# 1) A negative root located between -R and -1
# 2) A first positive root located between -1 and R
# 3) A second positive root located after R and just before a big number (I used 5*R in this case)
L = [-R, -1, -1, R, R, 5*R]

# Calculate solutions
c1 = bisection_method(L[0], L[1], errorTolerance, maxIterations)
c2 = bisection_method(L[2], L[3], errorTolerance, maxIterations)
c3 = bisection_method(L[4], L[5], errorTolerance, maxIterations)
    

# Display all solutions
print("Solution 1 =", c1, "given a0 =", L[0], "and b0 =", L[1])
print("Solution 2 =", c2, "given a0 =", L[2], "and b0 =", L[3])
print("Solution 3 =", c3, "given a0 =", L[4], "and b0 =", L[5])


# Graph results
X = np.linspace(-10, 10, 100)
Y = f(X)

fig, ax = plt.subplots()
ax.set_xlim(-4, 10)
ax.set_ylim(-255, 100)
ax.set_title("Volumen que falta llenar vs Nivel de agua")
ax.set_xlabel("Nivel de agua (m)")
ax.set_ylabel("Volumen falta llenar (m³)")

ax.plot(X, Y, 'tab:red')

# Inspired by https://matplotlib.org/api/_as_gen/matplotlib.pyplot.arrow.html
ax.annotate("Root 1", xy=(c1, f(c1)), xytext=(c1-2,1), arrowprops=dict(arrowstyle="->"))
plt.plot([c1], [f(c1)], marker='o', color='blue')
ax.annotate("Root 2", xy=(c2, f(c2)), xytext=(c2-2,2), arrowprops=dict(arrowstyle="->"))
plt.plot([c2], [f(c2)], marker='o', color='blue')
ax.annotate("Root 3", xy=(c3, f(c3)), xytext=(c3-2,3), arrowprops=dict(arrowstyle="->"))
plt.plot([c3], [f(c3)], marker='o', color='blue')

plt.show()
