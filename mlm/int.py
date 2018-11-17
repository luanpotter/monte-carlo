#!/bin/python

import random
import math
from base import mc

[ pi, sqrt, exp, ln ] = [ math.pi, math.sqrt, math.exp, math.log ]

sigma = 1/4
mu = 0
def f(x): return 1/(x*sigma*sqrt(2*pi))*exp((-(ln(x)-mu)**2)/(2*sigma**2))

def mc_it(it): return mc(f, 0, 2, 2, it)[0]
def run(it): print('%d : %s' % (it, mc_it(it)))

its = [ 9 ]
for it in its:
    run(10**it)
