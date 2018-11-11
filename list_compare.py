#!/usr/bin/env python3
# encoding: utf-8

import operator

def list_compare(a, b, op):
	if len(a) != len(b) and op is operator.eq or op is operator.ne:
		return op is operator.ne
	# search for the first index where items are different
	for i in range(len(a)):
		if a[i] != b[i]:
			break
	print(i)
	if i >= len(a) or i >= len(b):
		# no more items to compare — compare sizes
		return op(len(a), len(b))

	# we have an item that differs, shortcuts for EQ/NE
	if op is operator.eq:
		return False
	if op is operator.ne:
		return True

	# compare the final item again using the proper operator
	return op(a[i], b[i])
