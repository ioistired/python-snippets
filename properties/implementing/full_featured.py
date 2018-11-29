#!/usr/bin/env pytest
# encoding: utf-8

import py.test

class property:
	__slots__ = ('fget', 'fset', 'fdel')

	def __init__(self, fget, fset=None, fdel=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel

	def setter(self, func):
		self.fset = func
		return self

	def deleter(self, func):
		self.fdel = func
		return self

	def __get__(self, instance, owner):
		# if a is a property of A, A.a should not call the getter
		if instance is None:
			return self

		return self.fget(instance)

	def __set__(self, instance, value):
		return self.fset(instance, value)

	def __delete__(self, instance):
		return self.fdel(instance)

test = """
class A:
	@property
	def a(self):
		return self._a

	@a.setter
	def a(self, value):
		self._a = value

	@a.deleter
	def a(self):
		del self._a
"""

def _test_impl(property_class):
	g = dict(property=property_class)
	exec(test, g)

	A = g['A']
	a = A()

	assert type(A.a) is property_class

	assert not hasattr(a, '_a')

	a.a = 0
	assert hasattr(a, '_a')
	assert a.a == a._a == 0 != A.a

	del a.a
	assert not hasattr(a, '_a')

def test_builtin_property():
	import builtins
	_test_impl(builtins.property)

def test_my_property():
	_test_impl(property)
