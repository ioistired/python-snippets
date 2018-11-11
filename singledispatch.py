#!/usr/bin/env python3
# encoding: utf-8

from functools import singledispatch

@singledispatch
def foo(x):
	return 'x is something'

@foo.register(int)
def foo_int(x):
	return 'x is an int'

@foo.register(str)
def foo_string(x):
	return x
