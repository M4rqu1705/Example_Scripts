#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/07.txt") as fp:
        protein = fp.read().strip().upper()
        n = 1000000
        codon_table = {
                "A": 4,
                "R": 6,
                "N": 2,
                "D": 2,
                #  "B": 4,
                "C": 2,
                "Q": 2,
                "E": 2,
                #  "Z": 4,
                "G": 4,
                "H": 2,
                "I": 3,
                "L": 6,
                "K": 2,
                "M": 1,
                "F": 2,
                "P": 4,
                "S": 6,
                "T": 4,
                "W": 1,
                "Y": 2,
                "V": 4,
                "START": 1,
                "STOP": 3,
                }

        possibilities = codon_table["START"] % n

        for aa in protein:
            possibilities *= codon_table[aa] % n

        possibilities *= codon_table["STOP"] % n

        print(possibilities % n)



if __name__ == "__main__":
    main()

