#!/usr/bin/env python3
# encoding: utf-8

from functools import lru_cache

memo = lru_cache(maxsize=None)

def fact_(x, f):
	if x == 0:
		return 1
	return x * f(x-1, f)

def recur(f):
	return lambda *args: f(*args, f)

fact = recur(fact_)

fact1 = (lambda f: lambda x: f(x)(f))(lambda x: lambda f: 1 if x == 0 else x * f(x-1)(f))

countdown_ = lambda n, f: (  # broken
	n == 0 and print('lift off') or ((print(n) or f(n-1,f))
)

countdown_ = lambda n, f: (  # easier with ternary than truthiness
	print('lift off') if n == 0
	else print(n) or f(n-1,f)
)
countdown = recur(countdown_)

