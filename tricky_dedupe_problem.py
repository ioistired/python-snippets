#!/usr/bin/env python3

import inspect

# please deduplicate this decorator as much as possible
# rules: you may use the entire stdlib from 3.3+ and even third party modules
# (although my solution uses no more than one import from the stdlib)
#
# you should ideally deduplicate the two for loops and the two `return func(...)`s as well,
# though this is not strictly necessary (my solution does)
#
# don't worry about the rest of the code, just make sure the output is the same when you run this file

def wrap(func):
	if inspect.isgeneratorfunction(func):
		def inner(*args, **kwargs):
			try:
				if not get_connection():
					1/0
			except ZeroDivisionError:
				with pool() as conn:
					set_connection(conn)
					for x in func(*args, **kwargs):
						yield x
			else:
				for x in func(*args, **kwargs):
					yield x
	else:
		def inner(*args, **kwargs):
			try:
				if not get_connection():
					1/0
			except ZeroDivisionError:
				with pool() as conn:
					set_connection(conn)
					return func(*args, **kwargs)
			else:
				return func(*args, **kwargs)

	return inner

class pool:
	def __enter__(self):
		return 'connection'
	def __exit__(self, *excinfo):
		set_connection(None)
		print('the connection is now closed')

CONNECTION = None

def set_connection(connection):
	global CONNECTION
	CONNECTION = connection

def get_connection():
	return CONNECTION

@wrap
def gen(a, b):
	print("gen")
	print(" ", a, b)
	print(" ", get_connection())
	for x in "ab":
		yield x

@wrap
def func(a, b):
	print("func")
	print(" ", a, b)
	print(" ", get_connection())
	return "blah"

@wrap
def both(a, b):
	print("both")
	print(" ", a, b)
	for x in gen(a, b):
		pass

	func(a, b)

if __name__ == "__main__":
	for x in gen(1, 2):
		pass

	func(3, 4)

	both(5, 6)
