#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	def bar(self):
		super()
		return __class__

	def baz(self):
		return __class__

print(Foo().bar())
print(Foo().baz())
