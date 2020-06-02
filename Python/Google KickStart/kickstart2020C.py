#!/usr/bin/env python
# -*- coding: utf-8 -*-

def problem1():
    T = int(input().strip())

    for c in range(T):
        N, K = input().strip().split(' ')
        N = int(N)
        K = int(K)

        arr = list(map(lambda x: int(x), input().strip().split(' ')))
        reference = list(range(K, 0, -1))

        count_downs = 0

        for i in range(len(arr) - K + 1):
            if arr[i:i+K] == reference:
                count_downs += 1

        print('Case #{}: {}'.format(c+1, count_downs), flush=True)

def problem2():
    pass

def is_perfect_square(x):
    return bool((x) ** 0.5 == int((x) ** 0.5))

def problem3():
    T = int(input().strip())

    for c in range(T):
        N = int(input().strip())

        data = input().strip().split(" ")
        sequence = []
        for el in data:
            try:
                sequence.append(int(el))
            except:
                continue

        perfect_squares = 0

        i = 0
        while i < len(sequence):
            j = i + 1
            while j < len(sequence):
                if is_perfect_square(sum(sequence[i:j])):
                    perfect_squares += 1

                j += 1
            if is_perfect_square(sum(sequence[i:])):
                perfect_squares += 1

            i+=1

        print('Case #{}: {}'.format(c+1, perfect_squares), flush=True)

def sweetness_score(arr):
    total = 0
    for i in range(len(arr)):
        total += (-1) ** (i) * arr[i] * (i + 1)

    return total


def problem4():
    T = int(input().strip())

    for c in range(T):
        N, Q = input().strip().split(" ")
        N = int(N)
        Q = int(Q)

        arr = input().strip().split(" ")
        for i in range(len(arr)):
            arr[i] = int(arr[i])

        total = 0
        for i in range(Q):
            query = input().strip().split(" ")
            operation = query[0]
            if operation == "U":
                arr[int(query[1]) - 1] = int(query[2])
            elif operation == "Q":
                total += sweetness_score(arr[int(query[1]) - 1: int(query[2])])


        print('Case #{}: {}'.format(c+1, total), flush=True)



if __name__ == "__main__":
    problem4()
