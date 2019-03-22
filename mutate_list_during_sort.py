#!/usr/bin/env python3

"""
CPython implementation detail: While a list is being sorted, the effect of
attempting to mutate, or even inspect, the list is undefined. The C implementation of
Python makes the list appear empty for the duration, and raises ValueError if it can
detect that the list has been mutated during a sort.

https://docs.python.org/3.7/library/stdtypes.html#list.sort

This module is a continuation of inspect_list_during_sort.py in this repository.
It attempts to mutate a list during sorting.
"""

l = list(range(10, 0, -1))

def attempt_1(x):
	"""sort key that tries to mutate the list in memory as it's being sorted"""
	index = 10 - x
	l[index] += 1

	return x % 7  # this is still a sort key, after all

print('attempt 1:\n')
try:
	l.sort(key=attempt_1)
except Exception:
	import traceback
	traceback.print_exc()
	print()

# alright, that didn't work, but only cause the list appears to be empty during sort
# what if we were passed a reference instead?

from types import SimpleNamespace

l = [SimpleNamespace(x=x) for x in range(10)]
def attempt_2(obj):
	obj.x = str(obj.x)
	return int(obj.x) % 7

print('attempt 2:\n')
l.sort(key=attempt_2)
print(l)

# yeah, looks like it's we can mutate the list during sorting this way
# although you can argue that we haven't "mutated the list" because we haven't done any swaps/deletions/appends
# ourself
