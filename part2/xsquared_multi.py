#!/bin/python

import random
import math
import numpy as numpy

def r(): return random.random()
def f(x): return x ** 2
def did_hit(x, y): return y <= f(x)

def run(it):
  hits = 0
  for _ in range(it):
    [x, y] = [r(), r()]
    if (did_hit(x, y)): hits += 1
  return hits / it

def table():
  its = numpy.logspace(1, 7, num = 14).tolist()
  return [[ it, run(round(it)) ] for it in its]

def main():
  t = table()
  l = ['%s\t%s' % (r[0], r[1]) for r in t]
  s = '\n'.join(l)
  print(s)

main()
