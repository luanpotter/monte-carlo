#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: math.floor(6 * x) + 1

def run(i, fn):
  MAX = 10**5

  numbers = list(map(fn, map(lambda x: random.random(), range(1, MAX))))
  bins = list(set(numbers))
  r = {}

  for b in bins:
      r[b] = len([x for x in numbers if x == b])

  print(r)

run(10**6, f)
