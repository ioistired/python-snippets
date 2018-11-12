#!/usr/bin/env python3
# encoding: utf-8

class C:
	c = 1

	def foo(self):
		self.c = 2

x1 = C()
x2 = C()
x1.foo()
print(x1.c)
print(x2.c)
print(C.c)
