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

f = lambda x: math.floor(6 * x) + 1

def run(i, fn):
  MAX = 10**5

  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))

  avg = sum(numbers) / len(numbers)
  print('avg: %s' % avg)

  bins = list(set(numbers)) + [7]
  print(bins)

  plot(i, numbers, bins)

run('dados', f)

plt.show()
