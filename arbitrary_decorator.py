#!/usr/bin/env python3
# encoding: utf-8

"""
an attempt to use any arbitrary expression as a decorator

per
https://docs.python.org/3/reference/compound_stmts.html#function-definitions
, not all expressions can be used as decorators. Just
"@" followed by a (maybe dotted) identifier, followed by an argument
list.

goal is to see if it's still possible
"""

if not __debug__:
	raise AssertionError(
		'debug mode must be enabled for the tests to run')

def deco(func):
	"""
	a dumb decorator which causes all arguments to be ignored
	and returns 42
	"""
	def wrapped(*args, **kwargs):
		return 42
	return wrapped

@deco
def control():
	return -1

assert control() == 42

class InvalidDecoratorFactory(int):
	def __neg__(self):
		return deco

thing = InvalidDecoratorFactory()
def control_2():
	return -1

assert (-thing)(control_2)() == 42


try:
	compile("""
@-thing
def control_3():
	return -1
""", '<string>', 'exec')
except SyntaxError:
	pass
else:
	raise AssertionError('@-thing is valid, after all')

def id(x):
	return x

try:
	code = compile("""
@id(-thing)
def intervention():
	return -1
""", '<string>', 'exec')
except SyntaxError:
	raise AssertionError(
		'identity failed to circumvent the decorator restriction')

g = dict(id=id, thing=thing)
exec(code, g)
assert g['intervention']() == 42
