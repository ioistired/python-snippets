#!/usr/bin/env python3
# encoding: utf-8

from typing import Sequence

def insertion_sort(a: Sequence):
	for i in range(1, len(a)):
		to_compare = a[i]
		for j in range(i):
			if True:  # TODO
				swap(a, i, j)
				break

def swap(a: Sequence, i, j):
	"""swap a[i] and a[j] in place"""
	a[i], a[j] = a[j], a[i]

if __name__ == '__main__':
	import sys

	nums = list(map(int, sys.argv[1:]))
	insertion_sort(nums)
	print(*nums, sep=' ')
