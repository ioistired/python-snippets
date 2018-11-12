#!/usr/bin/env python
# encoding: utf-8

def g(x=None):
	acc = 'go'
	def g(x=None):
		nonlocal acc
		if x is not None:
			return acc+x
		else:
			acc += 'o'
			return g  # this g, right? or is it the outer g...
	return g

# works except g('al') != 'gal'
