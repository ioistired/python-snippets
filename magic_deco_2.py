#!/usr/bin/env python3
# encoding: utf-8

def inject_x(f):
	x = 'hi'
	def g(*args, **kwargs):
		nonlocal x
		return f(*args, **kwargs)
	return g

@inject_x
def foo():
	return x

def inject_x_attempt_2(f):
	def wrapper(f):
		x = 'hi'
		def wrapped(*args, **kwargs):
			nonlocal x
			return f(*args, **kwargs)
		return wrapped
	return wrapper(f)


@inject_x_attempt_2
def bar():
	return x


if __name__ == '__main__':
	try:
		print(foo())
	except NameError:
		print('attempt 1 failed')

	try:
		print(bar())
	except NameError:
		print('attempt 2 failed')

	try:
		print(baz())
	except NameError:
		print('attempt 3 failed')

	print(x)
