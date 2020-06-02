#!/usr/bin/env python
# -*- coding: utf-8 -*-

def permutations(n, a):
  all_permutations = []

  c = [0] * n

  all_permutations.append(a[:])

  i = 0
  while i < n:
    if c[i] < i:
      if i % 2 == 0:
        a[0], a[i] = a[i], a[0]
      else:
        a[c[i]], a[i] = a[i], a[c[i]]

      all_permutations.append(a[:])

      c[i] += 1
      i = 0
    else:
      c[i] = 0
      i += 1
  
  return all_permutations



def problem1():
  T = int(input().strip())

  for i in range(T):
    N, B = input().split(' ')
    N = int(N)
    budget = int(B)

    prices = input().strip().split(' ')

    for k, price in enumerate(prices):
      prices[k] = int(price)

    prices.sort()

    amount = 0
    for price in prices:
      if budget >= price:
          budget -= price
          amount += 1

    print('Case #{}: {}'.format(i+1, amount), flush=True)



    


problem1()
