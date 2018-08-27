#!/bin/python

from task01_4b_plot_ait import plot_ait

import random
import math
import numpy as np
import matplotlib.pyplot as plt

MAX = 10**3

theta = lambda x: math.pi * x
phi = lambda x: 2 * math.pi * x

alpha = lambda x: math.degrees(phi(x))
delta = lambda x: math.degrees(theta(x) - math.pi / 2)

run = lambda fn: list(map(fn, map(lambda x: random.random(), range(1, MAX))))

alphas = run(alpha)
deltas = run(delta)

plot_ait(np.array(alphas), np.array(deltas))
plt.show()
