#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**4
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

def nbinmaker(min_e, max_e, n, base = math.e):
  l_max_e = math.log(max_e, base)
  l_min_e = math.log(min_e, base)
  space = l_max_e - l_min_e
  x = (base - 1) * space / (math.pow(base, n) - 1)
  prev = l_min_e
  r = []
  for i in range(0, n + 1):
    r.append(prev)
    prev = prev + x * math.pow(base, n - 1 - i)
  r[len(r) - 1] = l_max_e + 1
  return r

def main():
  fn = energy
  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))
  min_e = min(numbers)
  max_e = max(numbers)
  bin_size = (max_e - min_e)/BINS

  bins = list(map(lambda x : min_e + x * bin_size, range(0, BINS)))
  lbins = nbinmaker(min_e, max_e, BINS)
  lnumbers = list(map(lambda x: math.log(x), numbers))

  freqs = []
  for idx, lbin in enumerate(lbins):
    if idx == len(lbins) - 1:
      break
    l = list(filter(lambda x: x >= lbin and x <= lbins[idx + 1], lnumbers))
    freqs.append(len(l))

  #lfreqs = list(map(lambda x: math.log(x), freqs))
  plot_log('energia (matplotlib log)', lnumbers)
  plot_bins('energia (a mao)', freqs, range(0, BINS))

main()
plt.show()
