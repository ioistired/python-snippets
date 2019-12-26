#!/usr/bin/env python3

class A:
	@staticmethod
	def foo():
		return 1

class B(A):
	@staticmethod
	def foo():
		return super().foo() + 1

print(B.foo())
