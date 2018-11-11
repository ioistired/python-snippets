#!/usr/bin/env python3
# encoding: utf-8


def is_palindrome(s: str) -> bool:
	if len(s) < 2:
		return True
	# this *is* tail call recursive
	# because of short circuiting on the LHS
	return s[0] == s[-1] and is_palindrome(s[1:-1])


def is_palindrome(s: str) -> bool:
	def aux(lo, hi):
		if (hi - lo) < 1:
			return True
		return s[lo] == s[hi] and aux(lo+1, hi-1)
	return aux(0, len(s)-1)


def is_palindrome(s: str, lo=0, hi=None) -> bool:
	hi = hi or len(s)-1
	if (hi - lo) < 1:
		return True
	return s[lo] == s[hi] and is_palindrome(s, lo+1, hi-1)


def is_palindrome(s: str, lo=0, hi=None) -> bool:
	hi = hi or len(s)-1
	return (hi - lo) < 1 or s[lo] == s[hi] and is_palindrome(s, lo+1, hi-1)

is_palindrome = (lambda f: lambda *args: f(*args, f))(lambda s, lo, hi, f:
	(lambda lo, hi: (hi-lo) < 1 or s[lo] == s[hi] and f(s,lo+1,hi-1,f))(0, hi or len(s)))

def is_palindrome(s: str, lo=0, hi=None) -> bool:
	return (lambda hi: (hi-lo) < 1 or s[lo] == s[hi] and is_palindrome(s,lo+1,hi-1))(hi or len(s)-1)

def is_palindrome(s: str, lo=0, hi=None) -> bool:
	if hi is None: hi = len(s)-1
	if hi - lo < 1:
		return True
	if s[lo].isspace(): lo += 1
	if s[hi].isspace(): hi -= 1
	return s[lo].lower() == s[hi].lower() and is_palindrome(s, lo+1, hi-1)


def to_exit_code(status: bool) -> int:
	# 0 = success
	# 1 = fail
	# (the opposite of py)
	return int(not status)


if __name__ == '__main__':
	import sys
	sys.exit(to_exit_code(is_palindrome(sys.argv[1])))
