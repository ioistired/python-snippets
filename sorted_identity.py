#!/usr/bin/env python3
# encoding: utf-8

"""
of course sorted makes a new copy of the list.
does it also preserve identity of the items?
"""

import random

if not __debug__:
	raise AssertionError(
		'debug mode must be enabled for the tests to run')

# control
nums = [random.randrange(100) for _ in range(10)]
assert sorted(nums) is not nums

class Sortable(int):
	pass

assert Sortable() is not Sortable()

# intervention
nums = list(map(Sortable, nums))
ids = sorted(map(id, nums))
assert ids == sorted(map(id, sorted(nums)))

# it does preserve identity of the items
