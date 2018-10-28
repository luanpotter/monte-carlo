#!/bin/python

import sys
import math
import numpy as np
from base import mc

vzero = -1
R = 0
a = 1
sax = lambda r: - vzero / (1 + math.exp((r - R)/a))

f = lambda b, it: (mc(sax, 0, b, None, it))[0]

bs = [ 1, 2, 10, 100, 1000 ]
its = [ 10**3, 10**5, 10**7, 10**8 ]

f2 = lambda b, _: b - np.log((1+math.exp(b))/2)

for b in bs:
    for it in its:
        print('b:%d, it:%d => r:%s' % (b, it, f2(b, it)))
        sys.stdout.flush()
