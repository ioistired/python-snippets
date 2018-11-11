#!/usr/bin/env python3
# encoding: utf-8

"""
itertools.count has an equivalent implementation listed in the docstring.
I just wanted to see if i could write that from memory.
"""

def count(start=0, step=1):
	i = start
	while True:
		yield i
		i += step
