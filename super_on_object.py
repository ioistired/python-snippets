#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	def bar(self):
		return super(object, self)

print(Foo().bar())
