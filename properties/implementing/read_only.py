#!/usr/bin/env python3
# encoding: ascii


class ReadOnlyProperty:
	def __init__(self, x):
		self.x = x

	@property
	def y(self):
		return self.x


x = ReadOnlyProperty(1)
assert x.y == 1
x.x = 2
assert x.y == 2

x.y = 3
