#!/usr/bin/env python3
# encoding: utf-8

class Foo:
	class __Bar: pass

if not __debug__:
	raise AssertionError('debug mode must be enabled for tests to run')

assert '__Bar' in dir(Foo)
