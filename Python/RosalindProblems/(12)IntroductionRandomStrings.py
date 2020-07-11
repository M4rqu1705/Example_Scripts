#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://rosalind.info/problems/prob/
import math

def main():
    def log(x):
        return math.log(x, 10)

    dna_string = "ACGATACAA"
    probabilities = [ float(prob) for prob in "0.129 0.287 0.423 0.476 0.641 0.742 0.783".split(" ") ]

    gc_count = 0
    for nucleotide in dna_string:
        if nucleotide == "G" or nucleotide == "C":
            gc_count += 1

    gc_content = gc_count / len(dna_string)

    for prob in probabilities:
        probability = 0
        for nucleotide in dna_string:
            if nucleotide == "A" or nucleotide == "T":
                probability += log( (1 - gc_content) / 2 * prob )
            elif nucleotide == "G" or nucleotide == "C":
                probability += log( gc_content / 2 * prob )

        print(probability)


if __name__ == "__main__":
    main()

