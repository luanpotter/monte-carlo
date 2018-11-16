#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

[ pi, sqrt, exp, ln ] = [ math.pi, math.sqrt, math.exp, math.log ]
def r(): return random.random()
def lmap(arr, fn): return list(map(fn, arr))

IT = 10**6

sigma = 1/4
mu = 0

def f(x): return 1/(x*sigma*sqrt(2*pi))*exp((-(ln(x)-mu)**2)/(2*sigma**2))

xs = np.linspace(0, 2, 1000).tolist()[1:]
ys = lmap(xs, f)

plt.plot(xs, ys, color='k')
plt.ylabel('f(x)')
plt.xlabel('x')

plt.tight_layout(0.5)
plt.savefig('mlm.png')
