#!/usr/bin/env python3
# encoding: utf-8

import ben


@ben.memoize
def fact(n):
	if n in (0, 1):
		return 1
	else:
		return n * fact(n - 1)

print(fact(99))
print(fact)
