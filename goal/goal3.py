#!/usr/bin/env python3
# encoding: utf-8

class _Goal:
	__slots__ = '_count'

	def __init__(self):
		self._count = 0

	def __call__(self, x=None):
		if x is None:
			# no args, add an "o"
			self._count += 1
			return self
		else:
			# allow re-use since this is supposed to be a singleton
			count = self._count
			result = 'g' + 'o'*count + x
			self._count = 0
			return result

g = _Goal()

if __name__== '__main__':
	print(g()('al'))
	print(g('al'))
	print(g()()()()()('al'))
