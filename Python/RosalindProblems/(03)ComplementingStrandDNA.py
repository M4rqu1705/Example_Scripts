#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/03.txt") as fp:
        string = ''.join(fp.readlines())
        complement = []

        for char in string[::-1]:
            if char == "A":
                complement.append("T")
            elif char == "T":
                complement.append("A")
            elif char == "G":
                complement.append("C")
            elif char == "C":
                complement.append("G")

        output = ''.join(complement)



        print(output)


if __name__ == "__main__":
    main()

