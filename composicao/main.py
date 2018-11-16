#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

[ pi, acos, sin, pow ] = [ math.pi, math.acos, math.sin, math.pow ]
def r(): return random.random()
def lmap(arr, fn): return list(map(fn, arr))

IT = 10**6
BINS = 10
alpha1 = 3 / (2*pi + 3)

def hist(name, values):
  plt.figure(figsize=(8,6))
  plt.hist(values, histtype='bar', rwidth=0.8, bins=BINS, color='gray')
  plt.xlabel(name)
  plt.ylabel('Frequência')
  plt.title('Histograma de %s' % name)
  plt.draw()

def plot(xs, ys):
  plt.plot(xs, ys, color='k')

def g1(u): return acos(1 - 2*u)/pi
def g2(u): return pow(u, 1/3)
def g(u1, u2): return g1(u2) if u1 <= alpha1 else g2(u2)
def gr(): return g(r(), r())

data = [gr() for _ in range(IT)]
hist('x', data)

def gdist(x): return (3 * pi)/(4 * pi + 6) * (sin(x * pi) + 4*x**2)
xs = np.linspace(0, 1, num = 1000).tolist()
normalize = IT/BINS
ys = lmap(xs, lambda x: normalize * gdist(x))
plot(xs, ys)

# plt.show()
plt.tight_layout(0.5)
plt.savefig('composicao.png')

