#!/usr/bin/env python3
# encoding: utf-8

from contextlib import AbstractContextManager

class identity(AbstractContextManager):
	def __init__(self, x):
		self.x = x
	def __enter__(self):
		return self.x
	def __exit__(self, *excinfo):
		pass

def test():
	class AttributeBox: pass
	x = AttributeBox()

	with identity(1) as x.y:
		pass

	assert x.y == 1

if __name__ == '__main__':
	test()
