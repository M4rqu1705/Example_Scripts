import math

# Function f(h) for the gap between the desired volume V and the volume obtained with the current
# water level h given a sperical tank of radius R

def f(h):
    return math.pi * h**3 - 3 * math.pi * R * h**2 + 3 * V


# Input some program requirements
#  errorTolerance = eval(input("What is the maximum accepted error tolerance between a and b?: "))
errorTolerance = 1E-10

#  maxIterations = eval(input("What is the maximum amount of iterations accepted?: "))
maxIterations = 1E10

#  V = eval(input("How much volume do you want to hold? (meters³): "))
V = 30

#  R = eval(input("What is the sperical tank's radius? (meters): "))
R = 3

# Use a = -1 as initial estimate as a lower value might result in an negative solution
a = -1
# Use b = R to adapt program to bigger and smaller tanks
b = R

# Initialize counter to track iterations
iterations = 0

# Print table header
print(" | %-4s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s | %-10s | "%("iter", "a", "c", "b", "f(a)", "f(c)", "f(b)", "error"))
print("-"*100)

# Use an error tolerance as stop criteria (Stop criteria #1) and max number of iterations (Stop
# criteria #3)
while abs(a - b) > errorTolerance and iterations < maxIterations:
    # Search for mid-point between a and b
    c = (a + b) / 2

    # Print table row
    print(" |  %-3d | %+-10.6f | %+-10.6f | %+-10.6f | %+-10.6f | %+-10.6f | %+-10.6f | %+-10.6f | "%(iterations+1, a, c, b, f(a), f(c), f(b), abs(a +- b)))

    # If a and c change signs (hence their product is negative), crop right side
    if f(a) * f(c) < 0:
        b = c

    # Otherwise, b and c changed signs and the left side must be cropped
    else:
        a = c

    # Increase iterations counter by 1
    iterations += 1


print("\nThe closest root of function f is between a =", -1, "and b =", R, "is x =", c)
