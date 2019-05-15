#!/usr/bin/env python3
# encoding: utf-8

"""
CLI tool to generate n x m matrices
perhaps useful to practice matrix ops on paper
"""

import random
import sys

if len(sys.argv) < 3:
	print('Usage:', sys.argv[0], '<width> <height>', file=sys.stderr)
	sys.exit(1)

n, m = map(int, sys.argv[1:3])
for row in range(m):
	for col in range(n):
		print(random.choice(range(10)), end=' ')
	print()
