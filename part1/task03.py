#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**5
BINS = 50
f = lambda x: -2.2*math.log(1 - x)

def plot(values):
  plt.hist(values, histtype='bar', rwidth=0.8, color='black', bins=BINS)
  plt.axvline(x=2.2)
  plt.xlabel('Tempo de Decaimento ($\\mu s$)')
  plt.ylabel('Frequência')
  plt.title('Histograma dos Tempos de Decaimento para $\\tau = 2,2$ μs')

def run(fn):
  numbers = list(map(fn, map(lambda x: random.random(), range(MAX))))
  avg = sum(numbers) / len(numbers)
  print(avg)
  plot(numbers)

run(f)
plt.savefig('task03.png')
