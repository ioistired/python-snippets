#!/usr/bin/env python3
# encoding: ascii

class Factorial:
	def __init__(self, n):
		if n < 0:
			raise ValueError
		self.n = n

	@property
	def value(self):
		if self.n == 0:
			return 1
		old_n = self.n

		self.n -= 1
		result = (self.n+1) * self.value

		self.n = old_n
		return result

if __name__ == '__main__':
	import sys

	print(Factorial(int(sys.argv[1])).value)
