#!/usr/bin/env python3
# encoding: utf-8
#
#  harmonic_series.py
# 
#  Benjamin Mintz, 2017
#
#  Public Domain

import unittest


def harmonic_series(n):
	"""not tail-call recursive"""
	
	if n == 1:
		return 1
	else:
		return 1/n + harmonic_series(n - 1)


def harmonic_series_tcr(n):
	"""tail-call recursive"""
	
	def aux(n, acc):
		if not isinstance(n, int):
			raise TypeError("n must be an integer")
		elif n < 1:
			raise ValueError("n must be positive") 
		elif n == 1:
			return acc
		else:
			return aux(n - 1, 1/n + acc)
	
	return aux(n, 1)


class HarmonicSeriesTests(unittest.TestCase):
	def test_harmonic_series(self):
		self.assertEqual(harmonic_series(3), 1 + 1/2 + 1/3)
		self.assertEqual(harmonic_series(1), 1)
	
	def test_harmonic_series_tcr(self):
		self.assertEqual(harmonic_series_tcr(3), 1 + 1/2 + 1/3)
		self.assertEqual(harmonic_series_tcr(1), 1)
		
		with self.assertRaises(TypeError):
			harmonic_series_tcr(-5.0)
		with self.assertRaises(ValueError):
			harmonic_series_tcr(0)
		
if __name__ == "__main__":
	import sys
	sys.exit(unittest.main(verbosity=2))
