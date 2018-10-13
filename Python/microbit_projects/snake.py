from microbit import *
import math

direction = 0
position = [0,0]

while True:
    if button_a.was_pressed():
        direction += 90
    elif button_b.was_pressed():
        direction -= 90


    position += math.cos(math.radians(direction)), math.sin(math.radians(direction))
    display.set_pixel(position[0]%5, position[1]%5, 0)

