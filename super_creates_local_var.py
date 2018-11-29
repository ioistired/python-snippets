#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	def bar(self):
		super()
		return __class__

	def baz(self):
		return __class__

	def quux(self):
		return '__class__' in locals()

	def waldo(self):
		# maybe accessing it from locals twice brings it in scope the second time
		return '__class__' in locals(), '__class__' in locals()

x = Foo()
for meth in x.bar, x.baz, x.quux, x.waldo:
	print(meth())

# output: Foo, Foo, False, (False, False)
