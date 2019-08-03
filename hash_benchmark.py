#!/usr/bin/env python3

import hashlib
import sys
import time

s = b'hello world'
try:
	algo = sys.argv[1]
	n = int(sys.argv[2])
except IndexError:
	print('Usage:', sys.argv[0], '<algo> <rounds>', file=sys.stderr)
	sys.exit(1)

t0 = time.perf_counter()
for _ in range(n):
	s = hashlib.new(algo, s).digest()
t1 = time.perf_counter()

print(t1 - t0, 'seconds')
