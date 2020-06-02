#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


# Helper functions
def permutations(n, a):
    all_permutations = []

    c = [0] * n

    all_permutations.append(a[:])

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                a[0], a[i] = a[i], a[0]
            else:
                a[c[i]], a[i] = a[i], a[c[i]]

            all_permutations.append(a[:])

            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return all_permutations


def problem1():
    T = int(input().strip())

    for i in range(T):
        N = int(input().strip())

        points = input().strip().split(' ')

        for j, point in enumerate(points):
            points[j] = int(point)

        peaks = 0
        for j, point in enumerate(points):
            if j == 0 or j == len(points) - 1:
                continue
            elif points[j-1] < point and point > points[j+1]:
                peaks += 1

        print('Case #{}: {}'.format(i+1, peaks), flush=True)



def problem2():
    T = int(input().strip())

    for i in range(T):
        N, D = input().strip().split(' ')
        N = int(N)
        deadline = int(D)

        routes = list(map(int, input().strip().split(' ')))

        start_date = deadline
        for route in reversed(routes):
            # Check for the closest day we can travel
            start_date = start_date // route * route

        print('Case #{}: {}'.format(i+1, start_date), flush=True)



def problem3():
    # !! Memory Limit Exceeded !!
    T = int(input().strip())

    regex_pattern = re.compile(r'(\d)\(([NSEW]+)\)')

    for i in range(T):
        program = input().strip()

        match = regex_pattern.search(program)
        # Expand program
        while match:
            multiplier = match.group(1)
            pattern = match.group(2)
            program = program.replace(
                    '{}({})'.format(multiplier, pattern),
                    pattern * int(multiplier))

            match = regex_pattern.search(program)

        x, y = 1, 1
        for step in program:
            if step == 'N':
                y -= 1
            elif step == 'S':
                y += 1
            elif step == 'W':
                x -= 1
            elif step == 'E':
                x += 1

        if x <= 0:
            x = 10 ** 9 + x
        if y <= 0:
            y = 10 ** 9 + y

        print('Case #{}: {} {}'.format(i+1, x, y), flush=True)




def problem4():
    T = int(input().strip())

    for i in range(T):
        W, H, L, U, R, D = input().strip().split(' ')
        W = int(W)      # Total width
        H = int(H)      # Total height
        L = int(L)      # Top left hole x
        U = int(U)      # Top left hole y
        R = int(R)      # Bottom right hole x
        D = int(D)      # Bottom right hole y

        x, y = 1, 1


        def travel(W, H, L, U, R, D, x, y):
            # Safe and sound
            if R < x and D < y:
                return 1
            # INSIDE HOLE
            elif L <= x and x <= R and U <= y and y <= D:
                return 0
            # On right edge
            elif x == W and y <= D:
                return travel(W, H, L, U, R, D, x, y+1)
            # On bottom edge
            elif y == H and x <= R:
                return travel(W, H, L, U, R, D, x+1, y)
            else:
                results = []
                results.append(travel(W, H, L, U, R, D, x+1, y))
                results.append(travel(W, H, L, U, R, D, x, y+1))

                return sum(results) / len(results)


        results = travel(W, H, L, U, R, D, x, y)
        #  breakpoint()

        print('Case #{}: {}'.format(i+1, results))



problem4()
