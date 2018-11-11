#!/usr/bin/env python3
# encoding: utf-8
#
#  triangle_number.py
#  
#  Benjamin Mintz, 2017
#  
#  Public Domain

from ben import memoize

import unittest

@memoize
def triangle_number(n):
	if n == 1:
		return 1
	else:
		return n + triangle_number(n - 1)


def triangle_number_tcr(n):
	def aux(n, acc):
		if n == 1:
			return acc
		else:
			return aux(n - 1, n + acc)
	
	return aux(n, 1)
	

class TriangleNumberTests(unittest.TestCase):
	def test_triangle_number(self):
		for i in range(20):
			self.assertEqual(triangle_number(i), i * (i + 1) // 2)


if __name__ == '__main__':
	import sys	
	sys.exit(unittest.main(verbosity=2))
