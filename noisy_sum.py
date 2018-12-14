#!/usr/bin/env python3
# encoding: utf-8

# goal is to get sum() to print what it's summing

nums = range(10)

class NoisyInt(int):
	def __add__(self, other):
		print(self, '+', other)
		return super().__add__(other)

	__radd__ = __add__

if __name__ == '__main__':
	print('sum(range(10)):')
	print(sum(map(NoisyInt, range(10))))

	print('sum(sys.stdin):')

	import sys
	print(sum(map(NoisyInt, sys.stdin)))
