#!/usr/bin/env python3
# encoding: utf-8

"""
get the reference count of an object
behavior is only defined for a non-debug build of CPython
"""

import ctypes
import struct
import sys

def refcount(x):
	# the first member of the object struct in CPython is an ssize_t refcount
	# assume there are no 128 bit machines, so ssize_t is either 8 or 4
	max_ssize_t = 8

	# assume builtins.id returns a pointer (CPython implementation detail)
	ptr = id(x)
	del x

	x_raw = ctypes.string_at(ptr, max_ssize_t)

	# refcount added by calling this function
	our_refcount = 1
	refcount, = struct.unpack_from('n', x_raw)
	return refcount - our_refcount

def test():
	x = object()
	assert refcount(x) == 1

	y = object()
	z = y
	assert refcount(y) == 2

if __name__ == '__main__':
	test()
