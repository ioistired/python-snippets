#!/usr/bin/env python3
# encoding: utf-8

def palindrome(s, lo=0, hi=None):
	if hi is None:
		hi = len(s) - 1
	if hi - lo < 2:
		return True
	a, b = s[lo], s[hi]
	if a.isspace():
		return palindrome(s, lo+1, hi)
	if b.isspace():
		return palindrome(s, lo, hi-1)
	return a == b and palindrome(s, lo+1, hi-1)


if __name__ == '__main__':
	import sys
	sys.exit(int(not palindrome(' '.join(sys.argv[1:]))))
