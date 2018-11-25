#!/bin/python

from ait import plot_ait
from exposicao import omega

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 5*10**3
D = 1

theta = lambda x: math.acos((math.sqrt(1 - 4*D*x + D**2 + 2*D)  - 1)/ D)
phi = lambda x: 2 * math.pi * x

alpha = lambda x: math.degrees(phi(x))
delta = lambda x: math.degrees(math.pi/2 - theta(x))

run = lambda fn: list(map(fn, map(lambda x: random.random(), range(MAX))))

alphas = run(alpha)
deltas = run(delta)

plot_ait(np.array(alphas), np.array(deltas))
plt.savefig('ait_dipolo.png')
