#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/04.txt") as fp:
        lines = fp.read().split("\n")
        genome = lines[0].strip()
        motif = lines[1].strip()
        positions = []

        for i in range(len(genome) - len(motif)):
            begin = i
            end = i + len(motif)
            if genome[begin: end] == motif[:]:
                positions.append(str(i + 1))


        print(" ".join(positions))


if __name__ == "__main__":
    main()

