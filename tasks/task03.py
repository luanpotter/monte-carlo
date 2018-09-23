#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

def plot(i, values):
  plt.figure(i)
  plt.hist(values, histtype='bar', rwidth=0.8)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('Histogram %s' % i)
  plt.legend()
  plt.draw()

f = lambda x: -2.2*math.log(1 - x)

def run(i, fn):
  MAX = 10**5

  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))

  avg = sum(numbers) / len(numbers)
  print('avg: %s' % avg)

  plot(i, numbers)

run('f', f)

plt.show()
