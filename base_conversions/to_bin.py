#!/usr/bin/env python3
# encoding: utf-8

def int_to_bin(n: int):
	mask = 1 << 32
	while mask > 0:
		if (n & mask) == 0:
			yield '0'
		else:
			yield 1

		mask >>= 1

if __name__ == '__main__':
	import sys
	n = int(sys.argv[1], base=0)
	for digit in int_to_bin(n):
		print(digit, end='')
	print()
