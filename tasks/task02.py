#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = None

def plot(i, values):
  plt.figure(i)
  plt.hist(values, histtype='bar', rwidth=0.8)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Histogram %s' % i)
  plt.legend()
  plt.draw()

energy = lambda x: math.pow(1 - x, -1.0/1.6)

def run(i, fn, start, end):
  MAX = 10**5
  HIST_RANGES = 10

  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))
  filtered = list(filter(lambda x: MAX == None or x < MAX, numbers))

  avg = sum(numbers) / len(numbers)
  print('avg: %s' % avg)

  plot(i, filtered)

run('energy', energy, 0, 1)

plt.show()
