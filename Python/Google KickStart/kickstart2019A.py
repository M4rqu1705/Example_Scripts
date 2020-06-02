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
    N, Q = input().strip().split(' ')
    N = int(N)
    Q = int(Q)

    chars = input().strip()

    yes = 0

    for j in range(Q):
      start, end = input().strip().split(' ')
      start = int(start)
      end = int(end)

      answer = [char for char in chars[start - 1:end]]

      if end - 1 == start:
        yes += 1
        continue
      elif end == start:
        continue

      all_permutations = permutations(end - start + 1, answer)

      for permutation in all_permutations:
        if permutation == permutation[::-1]:
          yes += 1
          break

    print('Case #{}: {}'.format(i+1, yes), flush=True)

def problem2():
  T = int(input().strip())

  for i in range(T):
    N = input().strip()
    N = int(N)

    energy_stones = []
    for j in range(N):
        energy_stone = input().strip().split(' ')
        energy_stone[0] = int(energy_stone[0])
        energy_stone[1] = int(energy_stone[1])
        energy_stone[2] = int(energy_stone[2])
        energy_stones.append(list(energy_stone))

    combinations = permutations(len(energy_stones), energy_stones)

    for k, combination in enumerate(combinations):
        total_energy = 0
        time_taken = 0

        for energy_stone in combination:
            # Eat amount of energy in stone minus drained energy from stone with a cap of 0
            total_energy += max(energy_stone[1] - time_taken * energy_stone[2], 0)
            time_taken += energy_stone[0]

        combinations[k] = [total_energy, tuple(combination)]

    maximum = max(combinations, key=lambda x: x[0])

    print('Case #{}: {}'.format(i+1, maximum[0]), flush=True)


problem2()
