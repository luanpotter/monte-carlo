#!/bin/python

from ait import plot_ait
from exposicao import omega

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**4
D = 1

theta = lambda x: math.acos((math.sqrt(1 - 4*D*x + D**2 + 2*D)  - 1)/ D)
phi = lambda x: 2 * math.pi * x

alpha = lambda x: math.degrees(phi(x))
delta = lambda x: math.degrees(math.pi / 2 - theta(x))

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

print('Selected points %d' % len(r[0]))
plot_ait(np.array(r[0]), np.array(r[1]))
plt.savefig('ait_dip2.png')
