#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/01.txt") as fp:
        string = ''.join(fp.readlines())

        A, G, C, T = 0, 0, 0, 0

        for char in string:
            if char == "A":
                A += 1
            elif char == "G":
                G += 1
            elif char == "C":
                C += 1
            elif char == "T":
                T += 1

        print(f"{A} {C} {G} {T}")


if __name__ == "__main__":
    main()

