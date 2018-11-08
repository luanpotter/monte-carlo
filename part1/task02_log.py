#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**4
BINS = 100

def plot_log(values):
  plt.hist(values, histtype='bar', bins=BINS, log=True, color='black')
  plt.ylabel('Frequência (log)')
  plt.xlabel('Energia (log)')
  plt.title('Histograma log(Energia)')
  plt.legend()
  plt.draw()
  plt.show()

energy = lambda x: math.pow(1 - x, -1.0/1.6)
log_energy = lambda x: math.log(energy(x))

def main():
  numbers = list(map(log_energy, map(lambda x: random.random(), range(1, MAX))))
  plot_log(numbers)

main()
