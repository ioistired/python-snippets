#!/usr/bin/env python3
# encoding: utf-8

# It is possible (though not recommended!) for the __del__() method
# to postpone destruction of the instance by creating a new reference to it.
# This is called object resurrection.
# It is implementation-dependent whether __del__() is called a second time
# when a resurrected object is about to be destroyed;
# the current CPython implementation only calls it once.
# https://docs.python.org/3/reference/datamodel.html#object.__new__

class Leak:
	def __del__(self):
		print('refcount = 0')
		self.self = self

import sys
x = Leak()
print(sys.getsizeof(x))
del x

import gc
assert gc.collect(), 'there should be an unreachable object'
