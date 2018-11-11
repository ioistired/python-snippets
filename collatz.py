#!/usr/bin/env python3
# encoding: utf-8
#
#  collatz.py
#  
#  Benjamin Mintz, 2017
#  Public Domain

#~ from ben import memoize

import unittest


def collatz_next(n):
	if n < 1:
		raise ValueError("n must be >= 1")
	elif type(n) is not int:
		raise TypeError("n must be an integer")
	elif n == 1:
		return 1
	elif n % 2:
		# 3n + 1 is always even
		# so skip the next value
		#~ return (3 * n + 1) // 2
		
		# never mind, i like seeing the extra steps
		return 3 * n + 1
	else:
		return n // 2

#~ @memoize
def collatz_sequence(n):
	"""
	returns the hailstone sequence of n
	if the collatz conjecture is true,
	collatz_sequence(n)[-1] is always 1
	(for positive integers n)
	"""
	
	def aux(n, seq):
		# since "and" is short-circuiting,
		# seq[-1] will never be evaluated
		# on an empty list
		if len(seq) > 0 and seq[-1] == 1:
			return seq
		else:
			return aux(collatz_next(n), seq=seq + [n])
	
	return aux(n, [])


class CollatzTests(unittest.TestCase):
	def test_collatz_next(self):
		tests = \
		(
			(27, 82),
			(1, 1),
			(16**2, 128),
		)
		
		for test, expected_output in tests:
			self.assertEqual(collatz_next(test), expected_output)
	
	def test_collatz_sequence(self):
		twenty_seven = collatz_sequence(27)
		
		# <https://en.wikipedia.org/wiki/Collatz_conjecture#Examples>
		tests = \
		(
			# wikipedia's length excludes the first num
			(len(twenty_seven), 112),
			(max(twenty_seven), 9232),
			(collatz_sequence(1), [1]),
			(collatz_sequence(12), [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]),
		)
		
		for test, expected_output in tests:
			self.assertEqual(test, expected_output)


if __name__ == '__main__':
	import sys
	sys.exit(unittest.main(verbosity=2))
