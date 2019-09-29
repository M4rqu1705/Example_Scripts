from microbit import *

while True:
    output = 'O'
    if button_a.is_pressed():
        output = 'A'
    elif button_b.is_pressed():
        output = 'B'

    display.show(output)

    sleep(50)

