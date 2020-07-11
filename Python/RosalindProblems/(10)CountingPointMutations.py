#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/10.txt") as fp:
        sequence1, sequence2 = fp.read().strip().split("\n")

        hamming_distance = 0
        for i in range(len(sequence1)):
            if sequence1[i] != sequence2[i]:
                hamming_distance += 1

        print(hamming_distance)



if __name__ == "__main__":
    main()

