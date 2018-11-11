#!/usr/bin/env python3
# encoding: utf-8

import inspect
import sys

# https://github.com/Rapptz/discord.py/blob/e2de93e2a65960c9c83e8a2fe53d18c4f9600196/discord/ext/commands/bot.py#L41-L53
def _get_variable(name):
	stack = inspect.stack()
	try:
		for frames in stack:
			try:
				frame = frames[0]
				current_locals = frame.f_locals
				if name in current_locals:
					return current_locals[name]
			finally:
				del frame
	finally:
		del stack

def inject_x(f):
	def g(*args, **kwargs):
		x = 'hi'
		return f(*args, **kwargs)
	return g

def foo():
	try:
		return x
	except NameError:
		print('x not in locals')
		return _get_variable('x')

def inject_x_attempt_2(f):
	f.__globals__['x'] = 'hi'
	return f

def inject_x_attempt_3(f):
	for frames in inspect.stack():
		frame = frames[0]
		if frame.f_code is f.__code__:
			frame.f_locals['x'] = 'hi'
	return f

# bar = inject_x_attempt_2(foo)
baz = inject_x_attempt_3(foo)

def inject_x_attempt_4():
	inject_x_attempt_3(inject_x_attempt_4)
	print(x)

def inject_x_attempt_5(f):
	def wrapper(f):
		x = 1
		def wrapped(*args, **kwargs):
			nonlocal x
			return f(*args, **kwargs)
		return wrapped
	return wrapper(f)

quux = inject_x_attempt_5(foo)
foo = inject_x(foo)

if __name__ == '__main__':
	print(foo())
	print(baz())
	# print(inject_x_attempt_4())
	print(quux())
	print(x)

