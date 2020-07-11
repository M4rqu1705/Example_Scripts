#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyboard
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase
print(alphabet)

count = 0

def callback(e):
    global count

    if e.name in alphabet:
        char = e.name
        if count % 2 == 0:
            char = char.lower()
        else:
            char = char.upper()

        #  pag.write(f'\b{char}')
        keyboard.write(f'\b{char}')

        count += 1



keyboard.on_press(callback)


while True:
    pass

