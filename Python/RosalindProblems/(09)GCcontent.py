#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/09.txt") as fp:
        lines = fp.read().strip().split("\n")
        dna_strings = {}

        # Assemble DNA strings with corresponding labels from data
        i = 0
        while i < len(lines):
            if lines[i].startswith(">"):
                label = lines[i][1:]
                dna_string = lines[i+1]
                j = 2
                while i + j < len(lines) and not lines[i + j].startswith(">"):
                    dna_string += lines[i+j]
                    j += 1

                dna_strings[label] = dna_string
                i += j
            else:
                i += 1


        # Calculate gc content and determine the greatest
        max_label = ""
        max_gc = 0
        
        for label, sequence in dna_strings.items():
            gc_count = 0

            for nucleotide in sequence:
                if nucleotide == "C" or nucleotide == "G":
                    gc_count += 1

            gc_content = gc_count / len(sequence) * 100

            if gc_content > max_gc:
                max_label = label
                max_gc  = gc_content

        print(f'{max_label}\n{round(max_gc, 6)}')


if __name__ == "__main__":
    main()

