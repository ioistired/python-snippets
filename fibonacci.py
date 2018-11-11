#!/usr/bin/env python3
# encoding: utf-8
#
#  fibonacci.py
#  
#  Benjamin Mintz, 2017
#  
#  Public Domain

#~ import ben

import unittest


def fib(n, start=(0, 1)):
	"""iterative fibonacci function"""
	a, b = start
	while n > 0:
		a, b = b, a + b
		n -= 1
	return n


def fib(n, start=(0, 1)):
	"""tail-recursive fibonacci function"""
	def aux(n, a, b):
		if n > 0:
			return aux(n - 1, b, a + b)
		else:
			return a
	
	return aux(n, *start)


class FibonacciTests(unittest.TestCase):
	def test_fib(self):
		
		# <https://oeis.org/A000045/list>
		sequence_through_38 = \
		(
			0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987, 1597,2584,4181,
			6765,10946,17711,28657,46368,75025, 121393,196418,317811,514229,
			832040,1346269, 2178309,3524578,5702887,9227465,14930352,24157817,
			39088169,
		)
		
		for n, fib_n in enumerate(sequence_through_38):
			self.assertEqual(fib(n), fib_n)


if __name__ == '__main__':
	import sys
	sys.exit(unittest.main(verbosity=2))
