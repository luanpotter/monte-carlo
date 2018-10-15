#!/bin/python

import math
from base import mcp

fn = lambda x: x**2
mcp(fn, 2, 3)

vzero = 1
R = 0
a = 1
sax = lambda r: - vzero / (1 + math.exp((r - R)/a))
sax_norm = lambda r: vzero + sax(r)
mcp(sax_norm, 0, 8)
