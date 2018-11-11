#!/usr/bin/env python3
# encoding: utf-8

if not __debug__:
	raise AssertionError('debug mode must be enabled for the tests to run')

class Messageable:
	def send(self): return 0

class User(Messageable):
	pass

class HookedMessageable(Messageable):
	def send(self): return super().send() + 1

# patch it
User.__bases__ = (HookedMessageable,) + User.__bases__

assert User().send() == 1
