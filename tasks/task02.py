#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

def plot(i, values, bins):
  plt.figure(i)
  plt.hist(values, bins, histtype='bar', rwidth=0.8)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Histogram %s' % i)
  plt.legend()
  plt.draw()

energy = lambda x: math.pow(1 - x, 1.6)

def run(i, fn, start, end):
  MAX = 10**5
  HIST_RANGES = 10

  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))
  ranges = list(map(lambda i: start + i*(end - start)/HIST_RANGES, range(0, HIST_RANGES + 1)))
  freq = { k: 0 for k, v in enumerate(ranges) }

  for n in numbers:
      r = next(i for i, r in enumerate(ranges) if n <= r)
      freq[r -  1] += 1

  avg = sum(numbers) / len(numbers)

  print(freq)
  print('avg: %s' % avg)

  plot(i, numbers, ranges)

run('energy', energy, 0, 1)

plt.show()
