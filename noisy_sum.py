#!/usr/bin/env python3
# encoding: utf-8

# goal is to get sum() to print what it's summing
# i want to see if it's lazy or gathers through the whole iterable first
# especially with sys.stdin

nums = range(10)

class NoisyInt(int):
	def __add__(self, other):
		print(self, '+', other)
		return super().__add__(other)

	# radd is necessary since sum is foldl (+) 0
	# where 0 is a regular int, not a NoisyInt
	__radd__ = __add__

if __name__ == '__main__':
	print('sum(range(10)):')
	print(sum(map(NoisyInt, range(10))))

	print('sum(sys.stdin):')

	import sys
	print(sum(map(NoisyInt, sys.stdin)))
