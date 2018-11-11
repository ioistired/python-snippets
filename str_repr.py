#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	def __str__(self):
		return 'str'

	def __repr__(self):
		return 'repr'

x = Foo()
print(x)
