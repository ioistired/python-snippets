#!/usr/bin/env python3

class TestDescriptor:
	def __get__(self, instance, owner):
		print(instance, owner)
		return 1

	def __set_name__(self, owner, name):
		print(f'{owner}.{name} = {self}')

class Foo:
	x = TestDescriptor()
