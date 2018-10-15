#!/bin/python

import math
from base import mcp

print('(a)')
mcp(lambda x: x**2)

print('(b)')
mcp(lambda x: x**4)

print('(c)')
mcp(lambda x: x**6)

print('(d)')
mcp(lambda x: math.sin(x))

print('(e)')
mcp(lambda x: math.cos(x))
