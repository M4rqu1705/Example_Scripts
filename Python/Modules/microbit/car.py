from microbit import *
import random

class Car:
    def __init__(self):
        self.x = 2

    def reset(self):
        self.x = 2

    def left(self):
        self.x -= 1 if 0 < self.x else 0

    def right(self):
        self.x += 1 if self.x < 4 else 0

    def show(self):
        display.set_pixel(self.x, 4, 9)

class Opponent:
    def __init__(self, x):
        self.position = [x, random.randint(-10, -5)]

    def reset(self, x):
        self.position = [x, random.randint(-10, -5)]

    def update(self):
        self.position[1] += 1 if self.position[1] < 5 else 0
        return True if self.position[1] < 5 else False

    def show(self):
        if -5 < self.position[1] < 0:
            display.set_pixel(self.position[0], 0, 6 + self.position[1])
        elif 0 <= self.position[1]:
            display.set_pixel(self.position[0], self.position[1], 7)


def startup_sequence():
    # Create simple animation
    a = Image("00000:00000:00500:00000:00000")
    b = Image("00000:05550:05750:05550:00000")
    c = Image("55555:57775:57975:57775:55555")
    d = Image("77777:79997:79997:79997:77777")
    e = Image("99999:99999:99999:99999:99999")

    increase = [a, b, c, d, e]

    sleep(500)
    display.show(increase, delay=200)
    display.show(e)
    sleep(500)

def game_over_sequence(score):
    display.clear()

    # Create simple animation
    a = Image("00000:00000:00000:00000:00000")
    b = Image("33333:33333:33333:33333:33333")
    c = Image("66666:66666:66666:66666:66666")
    d = Image("99999:99999:99999:99999:99999")
    blink = [a, b, c, d, d, d, c, b, a]

    f = Image("99999:99999:99999:99999:99999")
    g = Image("77777:79997:79997:79997:77777")
    h = Image("55555:57775:57975:57775:55555")
    i = Image("00000:05550:05750:05550:00000")
    j = Image("00000:00000:00500:00000:00000")
    decrease = [f, g, h, i, j]

    for i in range(3):
        display.show(blink, delay=50)
    sleep(500)
    # Display score
    if score < 10:
        display.show(str(score))
        sleep(3000)
    else:
        sleep(500)
        display.scroll(str(score))
        sleep(500)
    display.scroll("Game Over")
    display.show(decrease, delay=200)
    display.clear()


car = Car()
opponents = [Opponent(0), Opponent(1), Opponent(2), Opponent(3), Opponent(4)]
interval_function = lambda c : (400 - c * 3) if c < 100 else 100
counter = 0

startup_sequence()

start_time = running_time()

while True:
    a, b = button_a.was_pressed(), button_b.was_pressed()

    if a != b:
        if a:
            car.left()
        elif b:
            car.right()
        continue
    else:
        display.clear()
        car.show()

        for opponent in opponents:
            if opponent.update():
                opponent.show()
                if opponent.position[1] == 4 and opponent.position[0] == car.x:
                    score = int((running_time() - start_time) / 1000)
                    game_over_sequence(score)

                    display.clear()
                    sleep(10000000)
            else:
                opponent.reset(opponent.position[0])

    counter += 1
    sleep(interval_function(counter))
