#!/bin/python

import random
import numpy as np
import matplotlib.pyplot as plt

def plot(i, values, bins):
  plt.figure(i)
  plt.hist(values, bins, histtype='bar', rwidth=0.8)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Histogram #%i' % i)
  plt.legend()
  plt.draw()

EXP = [ 1, 2, 3, 4, 6 ]

for i, exp in enumerate(EXP):
  print('Running for %s: ----------------' % exp)
  MAX = 10**exp
  HIST_RANGES = 10

  numbers = list(map(lambda x: random.random(), range(1, MAX)))
  ranges = list( map(lambda i: i/HIST_RANGES, range(1, HIST_RANGES + 1)))
  freq = { k: 0 for k, v in enumerate(ranges) }

  for n in numbers:
      r = next(i for i, r in enumerate(ranges) if n <= r)
      freq[r] += 1

  print(freq)

  avg = sum(numbers) / len(numbers)
  print('avg: %s' % avg)

  plot(i, numbers, [0] + ranges)

plt.show()
