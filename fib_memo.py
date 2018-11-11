#!/usr/bin/env python3
# encoding: utf-8

def memoize(f):
	class MemoDict(dict):
		def __init__(self, f):
			self.f = f
		def __call__(self, *args):
			return self[args]
		def __missing__(self, args):
			self[args] = ret = self.f(*args)
			return ret
	return MemoDict(f)


import functools


#~ @functools.lru_cache(maxsize=None)
@memoize
def fib(n):
	if n in (0, 1):
		return n
	else:
		return fib(n - 1) + fib(n - 2)


def main(args):
	import time
	start_time = time.clock()
	for i in range(2**24):
		fib(i)
	print(time.clock() - start_time)
	return 0

if __name__ == '__main__':
	import sys
	#~ sys.exit(main(sys.argv))
	for i in range(100):
		fib(i)
	print(fib(100))

known = {0: 0, 1: 1}
# infinite recursion for some reason
def fib(n):
	known[n] = ret = known.get(n, fib(n - 1) + fib(n - 2))
	print(known)
	return ret
