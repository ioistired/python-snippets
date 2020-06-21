#!/usr/bin/env python3

import contextlib

class _SymbolMeta(type):
	def __getattr__(cls, key):
		try:
			return cls._cache[key]
		except KeyError:
			rv = cls._cache[key] = cls(key)
			return rv

class Symbol(metaclass=_SymbolMeta):
	"""Brings LISP style symbols to Python.

	Symbol.x is an interned object. You can use it as a replacement for sys.intern('x') or object() in argument
	defaults. Symbol('x') also works.
	"""

	_cache = {}

	def __init__(self, key: str):
		self.key = key

	def __hash__(self):
		return hash((type(self), self.key))

	def __repr__(self):
		key = self.key
		cls_name = type(self).__qualname__
		if key.isidentifier():
			return f'{cls_name}.{key}'
		else:
			return f'{cls_name}({key!r})'

def test():
	x = Symbol.x
	y = Symbol.y
	assert x != y
	x2 = Symbol.x
	assert x2 is x
	d = {}
	d[x] = 1
	d[y] = 2
	assert d[x] != d[y]
	assert d[x] == d[x2]
	assert d[x] != d.get('x')
	assert d[y] != d.get('y')

if __name__ == '__main__':
	test()
