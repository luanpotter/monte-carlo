#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**5
BINS = 100

def plot_log(i, values):
  plt.figure(i)
  plt.hist(values, histtype='bar', bins=BINS, log=True)
  plt.xlabel('log x')
  plt.ylabel('log y')
  plt.title('Histogram log %s' % i)
  plt.legend()
  plt.draw()

def plot_bins(i, values, bins):
  plt.figure(i)
  plt.plot(bins, values, 'bo')
  plt.xlabel('log x')
  plt.ylabel('log y')
  plt.title('Histogram log %s' % i)
  plt.legend()
  plt.draw()

energy = lambda x: math.pow(1 - x, -1.0/1.6)

def main():
  fn = energy
  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))
  min_e = min(numbers)
  max_e = max(numbers)
  bin_size = (max_e - min_e)/BINS

  bins = list(map(lambda x : min_e + (x + 1) * bin_size, range(0, BINS)))
  lbins = list(map(lambda x: math.log(x), bins))

  freqs = []
  for idx, lbin in enumerate(lbins):
      l = list(filter(lambda x: x <= lbin and (idx == 0 or x > lbins[idx - 1]), numbers))
      freqs.append(len(l))
  print(freqs)

  lfreqs = list(map(lambda x: math.log(x), freqs))
  lnumbers = list(map(lambda x: math.log(x), numbers))
  plot_log('energia (matplotlib log)', lnumbers)
  plot_bins('energia (a mao)', lfreqs, lbins)

main()
plt.show()
