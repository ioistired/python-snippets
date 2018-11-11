#!/usr/bin/env python3
# encoding: utf-8

import functools

class Memoize(dict):
	def __init__(self, f):
		self.f = f
		self.cache = {}
		# copy __name__ and stuff
		functools.update_wrapper(self, f)

	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			# you might think that instead of using if/else we could use
			# dict.setdefault i.e. return self.cache.setdefault(args, f(*args))
			# however, that would eval f(*args) before calling setdefault
			# `return self.cache.setdefault(args, f(*args)) if args not in self.cache else self.cache[args]
			# would work too, but is less clear
			self.cache[args] = result = self.f(*args)
			return result

def fib(n):
	if n in (0, 1):
		return n
	else:
		return fib(n-1) + fib(n-2)

test_size = 30
print(f'unmemoized, fib({test_size}) =')
print(fib(test_size))

fib = Memoize(fib)
print(f'  memoized, fib({test_size}) =')
print(fib(test_size))
