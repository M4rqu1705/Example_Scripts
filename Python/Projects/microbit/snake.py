from microbit import *
import random

class Snake:
    def __init__(self):
        # Direction number responds to the following:
        # 0: top
        # 1: right
        # 2: bottom
        # 3: left
        self.direction = 1
        # Position is a list of coordinates for the snake's body
        self.position = [[0,0], [0,0]]

    def show(self):
        for position in self.position:
            display.set_pixel(position[0], position[1], 3)
        display.set_pixel(self.position[0][0], self.position[0][1], 6)

    def turn(self, side):
        if side == "right":
            self.direction += 1 if self.direction < 3 else -3
        elif side == "left":
            self.direction -= 1 if 0 < self.direction else -3

    def move(self):
        for c in range(-1, -(len(self.position)), -1):
            self.position[c][0] = self.position[c-1][0]
            self.position[c][1] = self.position[c-1][1]

        if self.direction == 0:
            self.position[0][1] -= 1 if 0 < self.position[0][1] else -4
        elif self.direction == 1:
            self.position[0][0] += 1 if self.position[0][0] < 4 else -4
        elif self.direction == 2:
            self.position[0][1] += 1 if self.position[0][1] < 4 else -4
        elif self.direction == 3:
            self.position[0][0] -= 1 if 0 < self.position[0][0] else -4

        self.show()


class Food:
    def __init__(self):
        self.position = [random.randint(0,4), random.randint(0,4)]

    def reset(self, exclude):
        self.position = [random.randint(0,4), random.randint(0,4)]
        while self.position in exclude:
            self.position = [random.randint(0,4), random.randint(0,4)]

    def show(self):
        display.set_pixel(self.position[0], self.position[1], 9)


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
        display.show(score)
    else:
        display.scroll(score)
    display.scroll("Game Over")
    display.show(decrease, delay=200)
    display.clear()


snake = Snake()
food = Food()

# PROGRAM BEGINS HERE --- PROGRAM BEGINS HERE --- PROGRAM BEGINS HERE
startup_sequence()

display.clear()
snake.show()
food.show()
sleep(1000)

while True:
    a, b = button_a.was_pressed(), button_b.was_pressed()

    if a != b:
        if a:
            snake.turn("left")
        elif b:
            snake.turn("right")
    else:
        display.clear()
        snake.move()
        food.show()

        if snake.position[0] in snake.position[1:]:
            game_over_sequence(len(snake.position))
            break

        if snake.position[0] == food.position:
            # Add a unit to the snake's length
            snake.position.append(list(snake.position[-1]))
            # Reposition the fruit to a place it does not touch the snake
            food.reset(snake.position)
            # Display both once again
            display.clear(); snake.show(); food.show()

        sleep(500)
