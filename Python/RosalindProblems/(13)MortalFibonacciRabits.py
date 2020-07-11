#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    with open("datasets/13.txt") as fp:
        n, m = fp.read().split(" ")

        n = int(n)
        m = int(m)

        offspring = 1

        newborns, babies, adults = 0, 0, 1
        population = 0
        history = []

        for i in range(2, n+1):
            print(f'Month #{i}')
            # Kill old adults
            if len(history) >= m:
                adults -= history[-m]
                print(f'Killing {history[-m]} adults. {adults} left over')

            population = adults + newborns
            print(f'Population: {population}')
            history.append(population)

            babies = newborns

            # Left over adults reproduce
            newborns = adults * offspring

            # Babies grow up
            adults += babies

            print()



        print(population)









if __name__ == "__main__":
    main()

