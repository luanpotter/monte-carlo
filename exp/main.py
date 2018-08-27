#!/bin/python

import random
import numpy as np

MAX = 1000
HIST_RANGES = 10

numbers = list(map(lambda x: random.random(), range(1, MAX)))
ranges = list( map(lambda i: i/HIST_RANGES, range(1, HIST_RANGES + 1)))
freq = { k: 0 for k, v in enumerate(ranges) }

for n in numbers:
    r = next(i for i, r in enumerate(ranges) if n <= r)
    freq[r] += 1

print(freq)

avg = sum(numbers) / len(numbers)
print('avg: %s' % avg)
