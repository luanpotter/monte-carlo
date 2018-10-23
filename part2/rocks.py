#!/bin/python

import random
import math

IT = 10**6

def r(): return random.random()
def did_hit(x, y): return x**2 + y**2 < 1

def run(it):
    hits = 0
    for _ in range(it):
        [ x, y ] = [ r(), r() ]
        if (did_hit(x, y)): hits += 1
    return hits

def main(it):
    hits = run(it)
    p = hits / it
    pi = 4 * p
    return pi

def m():
    print('E1 : %s' % main(10**1))
    print('E4 : %s' % main(10**4))
    print('E6 : %s' % main(10**6))
    print('E9 : %s' % main(10**9))

m()
