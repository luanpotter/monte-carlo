#!/bin/python

import random
import math

IT = 10**7

def did_hit(fn):
  x = random.random()
  y = random.random()

  ty = fn(x)
  return y <= ty

def mc(fn):
  hits = 0
  for _ in range(0, IT + 1):
    if (did_hit(fn)):
      hits = hits + 1
  print('Hits %s' % hits)
  print('Total %s' % IT)
  print('Area %s' % (hits / IT))

fn = lambda x: x**2
mc(fn)
