import numpy as np

np.set_printoptions(precision=2)

width, height = 10, 15

top = 0
bottom = 50
left = 100
right = 25

top_left = (top + left) / 2
top_right = (top + right) / 2
bottom_left = (bottom + left) / 2
bottom_right = (bottom + right) / 2

# Add up all of the perimeter points
center_points = top_left + (width - 2) * top + top_right
center_points += (left + right) * (height - 2)
center_points += bottom_left + (width - 2) * bottom + bottom_right

# Average out by dividing by the perimeter size
center_points /= 2*(width + height)

# Compose multidimensional array
arr = np.array([
    [[top_left] + [top] * (width - 2) + [top_right]] +
    [[left] + [center_points] * (width - 2) + [right]]*(height - 2) + 
    [[bottom_left] + [bottom] * (width - 2) + [bottom_right]]
    ], dtype=float)

print(arr)
