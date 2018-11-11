#!/usr/bin/env python3
# encoding: utf-8

from collections import deque


def words(xs):
	result = deque()
	current = deque()
	for c in reversed(xs):  # like foldr
		if c != ' ':
			current.appendleft(c)
		elif current:
			result.appendleft(''.join(current))
			current.clear()
	return result


if __name__ == '__main__':
	import sys
	print(words(sys.argv[1]))
