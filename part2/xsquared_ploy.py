#!/bin/python

import random
import math
import numpy as numpy

xs = numpy.linspace(0, 1, 1000)
ys = xs ** 2
rs = numpy.column_stack([xs, ys])

for r in rs:
    print('%f\t%f' % (r[0], r[1]))
