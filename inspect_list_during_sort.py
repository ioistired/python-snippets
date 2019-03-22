#!/usr/bin/env python3

"""
CPython implementation detail: While a list is being sorted, the effect of
attempting to mutate, or even inspect, the list is undefined. The C implementation of
Python makes the list appear empty for the duration, and raises ValueError if it can
detect that the list has been mutated during a sort.

https://docs.python.org/3.7/library/stdtypes.html#list.sort
"""

make_l = lambda: list(range(10, -1, -1))
l = make_l()

def sort_key_peeker(x):
	print(l)
	return x

l.sort(key=sort_key_peeker)
# prints [] 10 times


## TODO attempt mutate during sort
