#!/bin/python

import random
import math
import numpy as numpy

IT = 10**6

def r(): return random.random()
def f(x): return x ** 2
def did_hit(x, y): return y <= f(x)

hits = 0
for _ in range(0, IT):
  [x, y] = [r(), r()]
  if (did_hit(x, y)): hits += 1

print(hits)
print(hits / IT)
