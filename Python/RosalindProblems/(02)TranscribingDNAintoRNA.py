#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/02.txt") as fp:
        string = ''.join(fp.readlines())

        list_string = [char for char in string]
        for i, char in enumerate(list_string):
            if char == "T":
                list_string[i] = "U"

        output = ''.join(list_string)


        print(output)


if __name__ == "__main__":
    main()

