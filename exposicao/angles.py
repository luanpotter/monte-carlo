#!/bin/python

from ait import plot_ait
from exposicao import omega

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**4

ctheta = lambda x: 2*x - 1
theta = lambda x: math.acos(ctheta(x))
phi = lambda x: 2 * math.pi * x

alpha = lambda x: math.degrees(phi(x))
delta = lambda x: math.degrees(theta(x) - math.pi / 2)

run = lambda fn: list(map(fn, map(lambda x: random.random(), range(MAX))))

alphas = run(alpha)
deltas = run(delta)

omegas_r = list(map(lambda d: omega(np.radians(d)), deltas))
omega_m = max(omegas_r)
omegas = list(map(lambda w: w/omega_m, omegas_r))

r = [[], []]
for i in range(MAX):
    alpha = alphas[i]
    delta = deltas[i]
    omega = omegas[i]
    if random.random() < omega:
        r[0].append(alpha)
        r[1].append(delta)

# plot_ait(np.array(alphas), np.array(deltas))
plot_ait(np.array(r[0]), np.array(r[1]))
# plt.show()
plt.savefig('ait.png')
