#!/usr/bin/env python3
# encoding: utf-8

import asyncio

# this code doesn't work
def asyncexecutor(*, timeout=None, loop=None, executor=None):
	"""decorator that turns a synchronous function into an async one

	Created by @Arqm#9302 (ID 325012556940836864). XXX Unknown license
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			partial = functools.partial(func, *args, **kwargs)
			loop = loop or asyncio.get_event_loop()	 # UnboundedLocalError here

			coro = loop.run_in_executor(executor, partial)
			# don't need to check if timeout is None since wait_for will just "block" in that case anyway
			return asyncio.wait_for(coro, timeout=timeout, loop=loop)
		return wrapper
	return decorator

def deco(*, loop=None):
	def wrapper(func):
		def wrapped(*args, **kwargs):
			loop = loop or asyncio.get_event_loop()
			return func(*args, **kwargs)
		return wrapped
	return wrapper

@deco()
def foo():
	return 'bar'

# foo() also errors

def f(loop=None):
	loop = loop or asyncio.get_event_loop()

f()  # does not error

def f(loop=None):
	def g():
		loop = loop or asyncio.get_event_loop()
	g()

# f()  # errors

# does the fix (nonlocal) permanently change x?
def f(x=None):
	def g():
		nonlocal x
		x = x or 1
	g()
	return x

print(f())  # 1
print(f(2))
print(f())


def deco(*, loop=None):
	def wrapper(func):
		def wrapped(*args, **kwargs):
			nonlocal loop
			loop = loop or asyncio.get_event_loop()
			print(loop)
		return wrapped
	return wrapper

@deco(loop=1)
def f():
	pass

f()

@deco(loop=2)
def f():
	pass

f()

@deco()
def f():
	pass

f()
