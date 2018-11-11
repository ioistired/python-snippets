#!/usr/bin/env python3
# encoding: utf-8

def foo():
	a = 1
	def bar(halt=False):
		if halt:
			return a  # fails here
		else:
			a = 2  # because of this
			return bar(True)
	return bar()

def foo1():
	a = 1
	def bar(halt=False):
		nonlocal a  # works now
		if halt:
			return a
		else:
			a = 2
			return bar(True)
	return bar()

if __name__ == '__main__':
	print(foo1())
	print(foo())
