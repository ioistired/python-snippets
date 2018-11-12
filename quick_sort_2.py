#!/usr/bin/env python3
# encoding: utf-8

from typing import Sequence


def quick_sort(t: Sequence, key=lambda x: x):
	t = t[:]  # dont mutate the original

	if len(t) < 2:
		return t

	pivot = (t[0] + t[len(t)//2] + t[-1]) // 3
	left = tuple(x for x in t if key(x) <= key(pivot))
	right = tuple(x for x in t if key(x) > key(pivot))
	print(left, pivot, right)
	return quick_sort(left) + quick_sort(right)


if __name__ == '__main__':
	import sys
	print(quick_sort(tuple(map(int, sys.argv[1:]))))
