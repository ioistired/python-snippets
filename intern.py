#!/usr/bin/env python3
# encoding: utf-8

class Interner(dict):
	def __missing__(self, key):
		self[key] = key
		return key

	def __call__(self, key):
		return self[key]


intern = Interner()
x = '你好'
y = '你好'.encode().decode()  # try to make a fresh string
assert x is not y
x = intern(x)
y = intern(y)
assert x is y
