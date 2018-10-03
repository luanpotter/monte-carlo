#!/bin/python

import random
import math

IT = 10**6

def did_hit(fn, a, b, maxy):
  x = a + (b - a) * random.random()
  y = maxy * random.random()

  ty = fn(x)
  return y <= ty

def mc(fn, a = 0, b = 1, maxy = None):
  maxy = maxy or fn(b)
  rectArea = (b - a) * maxy
  hits = 0
  for _ in range(0, IT):
    if (did_hit(fn, a, b, maxy)):
      hits = hits + 1
  intArea = rectArea * (hits / IT)
  print('Hits %s' % hits)
  print('Total %s' % IT)
  print('Area %s' % intArea)

fn = lambda x: x**2
mc(fn, 2, 3)
