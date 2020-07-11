#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/06.txt") as fp:
        n, k = fp.read().split(" ")

        n = int(n)
        k = int(k)

        i = 4
        a = 1
        b = 0
        pb = k
        pop = 1

        while i <= n:
            # Adults reproduce and produce b babies
            b = a * k

            # Previous babies grow
            a += pb

            # Population is the sum of all the babies and all the adults
            pop = b + a

            # The next loop's previous babies are this loop's babies
            pb = b

            i += 1

        print(pop)


if __name__ == "__main__":
    main()

