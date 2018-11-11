#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	def __init__(self):
		nonlocal bar
		bar = 1

	@classmethod
	def get_bar(cls):
		return cls.bar


if __name__ == '__main__':
	assert 'bar' not in globals()
	x = Foo()
	print(foo.get_bar())
	assert 'bar' not in globals()
