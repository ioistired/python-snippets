#!/usr/bin/env python3
# encoding: utf-8

# aids in testing by reducing the length of repr(n)
class Frozenset(frozenset):
	def __repr__(self):
		if not self:
			return '{}'  # incorrect, but aids in testing
		return (
			super().__repr__()
			.replace(type(self).__name__, '')
			.replace('(', '')
			.replace(')', '')
		)

	def __and__(self, other):
		return type(self)(super().__and__(other))

	def __or__(self, other):
		return type(self)(super().__or__(other))

ZERO = frozenset()

def succ(n):
	return n | frozenset({n})

ONE = succ(ZERO)

def encode(n):
	encoded = ZERO
	for _ in range(n):
		encoded = succ(encoded)
	return encoded

def pred(n):
	if n == ZERO:
		return ZERO

	raise NotImplementedError
