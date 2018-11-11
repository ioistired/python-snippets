#!/usr/bin/env python3
# encoding: utf-8

def binary_search_recursive(seq, key):
	def aux(lo, hi):
		if lo > hi:
			raise ValueError('{} is not in seq'.format(key))
		
		mid = (lo+hi)//2
		mid_val = seq[mid]
		
		if mid_val == key:
			return mid # found
		if mid_val < key:
			return aux(mid+1, hi) # search upper half
		if mid_val > key:
			return aux(lo, mid-1) # search lower half
		
	return aux(0, len(seq)-1)


def binary_search_iterative(seq, key):
	lo, hi = 0, len(seq)-1
	
	while lo <= hi:
		mid = (lo+hi)//2
		mid_val = seq[mid]
		
		if mid_val == key:
			return mid
		if mid_val < key:
			lo = mid + 1
		if mid_val > key:
			hi = mid - 1
	# lo > hi
	raise ValueError('{} is not in seq'.format(key))
