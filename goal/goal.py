#!/usr/bin/env python
# encoding: utf-8

def g(x=None, acc='g'):
	if x is None:
		def g(x=None):
			nonlocal acc
			if x is not None:
				return acc+'o'+x
			else:
				acc += 'o'
				return g
		return g
	return acc+x
