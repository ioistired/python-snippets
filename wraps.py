#!/usr/bin/env python3
# encoding: utf-8

import random
import sys
import time


def timeit(func):
	def timed(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		print(
			func.__name__,
			'ran in',
			time.time() - start_time,
			'seconds', file=sys.stderr)
		return result

	return timed


def wraps(func):
	def wrapped(func):
		def wrapped(*args, **kwargs):
			return func(*args, **kwargs)

	wrapped.__name__ = func.__name__
	wrapped.__doc__  = func.__doc__
	return wrapped


@timeit
def foo():
	time.sleep(random.random())
	return 1


print(foo())
print(foo.__name__)


def timeit(func):
	@wraps
	def timed(*args, **kwargs):
		start_time = time.time()
		result = func(*args, **kwargs)
		print(
			func.__name__,
			'ran in',
			time.time() - start_time,
			'seconds', file=sys.stderr)
		return result
	return timeit


@timeit
def foo():
	time.sleep(random.random())
	return 2


print(foo())
print(foo.__name__)
