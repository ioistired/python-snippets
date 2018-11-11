#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	pass

class Bar:
	baz = Foo

print(Bar().baz)

class Foo:
	def __call__(self, x):
		return 1

class Bar:
	baz = Foo

print(Bar().baz)
