#!/usr/bin/env python3
# encoding: utf-8

def foo():
	print('outer foo')
	def foo():
		print('inner foo')
		return foo
	return foo() is foo

print(foo())

# lesson: inner foo returned itself, not outer foo