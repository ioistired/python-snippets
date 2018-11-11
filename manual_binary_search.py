#!/usr/bin/env python3
# encoding: utf-8

import sys

lo, hi = map(int, sys.argv[1:3])

while True:
	mid = (lo+hi)//2
	print('Try ', mid)

	try:
		response = input('Too high or too low? (h/l) ')
	except EOFError:
		sys.exit(0)

	if response == 'h':
		hi = mid - 1
	elif response == 'l':
		lo = mid + 1
	else:
		sys.exit(1)
