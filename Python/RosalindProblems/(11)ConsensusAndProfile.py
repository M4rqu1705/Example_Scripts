#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/11.txt") as fp:
        lines = fp.read().strip().split("\n")
        dna_strings = {}

        i = 0
        while i < len(lines):
            if lines[i].startswith(">"):
                label = lines[i][1:]
                string = lines[i+1]
                j = 2
                while i + j < len(lines) and not lines[i + j].startswith(">"):
                    string += lines[i + j]
                    j += 1

                dna_strings[label] = string[:]
                i += 2
            else:
                i += 1

        # 4 by len(string) matrix of zeros
        matrix = [ [0 for i in range(len(string))] for i in range(4)]

        # Dictionary that assigns correspondence from nucleotide bases to their corresponding rows
        rows = {"A": 0, "C": 1, "G": 2, "T": 3}

        for label, string in dna_strings.items():
            # Iterate nucleotide for nucleotide
            for i in range(len(string)):

                nucleotide = string[i]
                # Add 1 to the corresponding row and column at the current position
                matrix[ rows[nucleotide] ][ i ] += 1



        # Find consensus string
        consensus = []
        reverse_rows = {0: "A", 1: "C", 2: "G", 3: "T"}
        for i in range(len(string)):
            quantities = [
                    matrix[0][i],
                    matrix[1][i],
                    matrix[2][i],
                    matrix[3][i],
                    ]
            
            max_index = quantities.index(max(quantities))
            consensus.append( reverse_rows[ max_index ] )


        print(''.join(consensus))
        for i, row in enumerate(matrix):
            print(f"{ reverse_rows[int(i)] }: { ' '.join(map(lambda x: str(x), row))} ")



if __name__ == "__main__":
    main()

