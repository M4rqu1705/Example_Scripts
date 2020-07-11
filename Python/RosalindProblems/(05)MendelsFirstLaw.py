#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/05.txt") as fp:
        k, m, n = fp.read().strip().split(" ")

        k = int(k)
        m = int(m)
        n = int(n)

        probs = []
        
        selection = ["k"] * k + ["m"] * m + ["n"] * n

        for i in range(len(selection)):
            for j in range(i+1, len(selection)):
                parents = [selection[i], selection[j]]

                if "k" in parents:
                    probs.append(1)
                elif "m" in parents and "n" in parents:
                    probs.append(0.50)
                elif "m" in parents:
                    probs.append(0.75)
                elif "n" in parents:
                    probs.append(0)

        print(round(sum(probs) / len(probs), 5))


if __name__ == "__main__":
    main()

