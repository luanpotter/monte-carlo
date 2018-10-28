#!/bin/python

import random
import math

IT = 10**6

def did_hit(fn, a, b, maxy):
  x = a + (b - a) * random.random()
  y = maxy * random.random()

  ty = fn(x)
  return y <= ty

def mc(fn, a = 0, b = 1, maxy = None, it = IT):
  maxy = maxy or max(fn(a), fn(b)) # specify maxy or function must be monotonic
  rectArea = (b - a) * maxy
  hits = 0
  for _ in range(it):
    if (did_hit(fn, a, b, maxy)):
      hits = hits + 1
  intArea = rectArea * (hits / it)
  return [ intArea, hits ]

def mcp(fn, a = 0, b = 1, maxy = None, it = IT):
  r = mc(fn, a, b, maxy, it)
  print('Hits %s' % r[1])
  print('Total %s' % it)
  print('Area %s' % r[0])
  return r[0]

def t2(h):
    a = h(0)
    b = h(1)
    m = min(a, b)
    M = max(a, b)

    alpha = 1/(M - m)
    beta = -m/(M - m)

    h_star = lambda x: alpha*h(x) + beta
    r = mc(h_star)
    return (M - m)*r[0] + m

def t2p(name, fn):
    print('%s: %s' % (name, t2(fn)))

def t3(h, a, b):
    nh = lambda z: h(a + (b - a)*z)
    return (b - a)*t2(nh)

def t3p(name, h, a, b):
    print('%s: %s' % (name, t3(h, a, b)))
