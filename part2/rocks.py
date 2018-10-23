#!/bin/python

import random
import math

IT = 10**6

def r():
    return random.random()

def did_hit(x, y):
    return x**2 + y**2 < 1

def run(it):
    hits = 0
    for _ in range(it):
        [ x, y ] = [ r(), r() ]
        if (did_hit(x, y)): hits += 1
    return hits

def main():
    hits = run(IT)
    p = hits / IT
    pi = 4 * p
    print(pi)

main()

