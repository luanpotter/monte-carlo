#!/bin/python

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**6
BINS = 10

r = lambda: random.random()
lmap = lambda arr, fn: list(map(fn, arr))

theta = lambda x: math.acos(1 - 2*x)
phi = lambda x: 2 * math.pi * x

run = lambda fn: lmap(lmap(range(MAX), lambda x: r()), fn)

n = MAX / BINS # normalization factor

thetas = run(theta)
plt.hist(thetas, color='grey', bins=BINS)
plt.plot([0, math.pi], [n, n], color='k') # this would be an ideal uniform pdf
plt.ylabel('Frequência')
plt.xlabel('$\\theta$')

plt.tight_layout(0.5)
plt.savefig('theta.png')

plt.clf()

phis = run(phi)
plt.hist(phis, color='grey', bins=BINS)
plt.plot([0, 2*math.pi], [n, n], color='k') # this would be an ideal uniform pdf
plt.ylabel('Frequência')
plt.xlabel('$\\phi$')

plt.tight_layout(0.5)
plt.savefig('phi.png')
