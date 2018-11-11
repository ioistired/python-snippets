#!/usr/bin/env python3
# encoding: utf-8
# Public Domain


def quick_sort(t):
	if len(t) < 2:
		return t
	
	# copy the list (don't modify it)
	t = t[:]
	
	# pick the middle element as the pivot
	pivot = t.pop((len(t) - 1)//2)
	
	left = list(filter(lambda x: x < pivot, t))
	right = list(filter(lambda x: x >= pivot, t))
	
	return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
	import random
	nums = [random.randrange(100) for _ in range(20)]
	
	print(quick_sort(nums))