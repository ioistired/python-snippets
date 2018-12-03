#!/usr/bin/env python3
# encoding: utf-8

# Douglas Crockford's idea for making generators
# basically "why do you need a `yield` keyword when you can just maintain some state"
# in my view, a class would be a better way to do this, and indeed, in python,
# that's how Iterators are defined.
def iter(list):
	i = 0
	def gen():
		nonlocal i
		value = list[i]
		i += 1
		return value
	return gen

gen = iter([1,2,3])
for _ in range(4):
	print(gen())
