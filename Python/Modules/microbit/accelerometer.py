from microbit import *

class MedianFilter():
    def __init__(self, length):
        self.length = length
        self.history = [0 for x in range(self.length)]

    def clean_history(self):
        self.history = [0 for x in range(self.length)]

    def add(self, value):
        self.history = self.history[1:]
        self.history.append(value)

    def get(self):
        array = sorted(self.history)
        if self.length % 2 == 0:
            middle1 = self.length // 2
            middle2 = middle1 + 1
            return (array[middle1] + array[middle2])/2
        else:
            middle = self.length // 2
            return array[middle]

x_filter = MedianFilter(9)
y_filter = MedianFilter(9)
maximum = 50

while True:
    if button_a.was_pressed():
        maximum -= 100
        x_filter.clean_history()
        y_filter.clean_history()
    elif button_b.was_pressed():
        maximum += 100
        x_filter.clean_history()
        y_filter.clean_history()

    # Retrieve and parse accelerometer values
    x = accelerometer.get_x()
    if abs(x) <= maximum:
        x_filter.add(x)
    else:
        if x < 0:
            x_filter.add(-maximum)
        else:
            x_filter.add(maximum)


    y = accelerometer.get_y()
    if abs(y) <= maximum:
        y_filter.add(y)
    else:
        if y < 0:
            y_filter.add(-maximum)
        else:
            y_filter.add(maximum)

    # Determine dot position in matrix
    divisor = (maximum*2)//5
    position = [(x_filter.get()+maximum)//divisor, (y_filter.get()+maximum)//divisor]

    # Safety measures
    if position[0] < 0:
        position[0] = 0
    elif 4 < position[0]:
        position[0] = 4

    if position[1] < 0:
        position[1] = 0
    elif 4 < position[1]:
        position[1] = 4

    # Update display
    display.clear()
    display.set_pixel(position[0], position[1], 9)

    sleep(20)
