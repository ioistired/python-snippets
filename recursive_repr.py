#!/usr/bin/env python3
# encoding: utf-8

class Factorial:
	__slots__ = ('n',)

	def __init__(self, n):
		self.n = n

	def __int__(self):
		if self.n < 2:
			return 1
		n = self.n
		self.n -= 1
		result = n * int(self)
		# put back the old n so this can be run multiple times
		self.n = n
		return result

	def __repr__(self):
		return str(int(self))


if __name__ == '__main__':
	print(repr(Factorial(5)))

