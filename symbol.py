#!/usr/bin/env python

class _SymbolMeta(type):
	def __getattr__(cls, key):
		return cls(key)

class Symbol(metaclass=_SymbolMeta):
	"""Brings LISP style symbols to Python.

	Symbol.x is an interned object. You can use it as a replacement for sys.intern('x') or object() in argument
	defaults. Symbol('x') also works.
	"""

	__slots__ = 'key',

	_cache = {}

	def __new__(cls, key: str):
		try:
			return cls._cache[key]
		except KeyError:
			self = cls._cache[key] = super().__new__(cls)
			self.key = key
			return self

	def __hash__(self):
		return id(self)

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
	assert x2 == x
	d = {}
	d[x] = 1
	d[y] = 2
	assert d[x] != d[y]
	assert d[x] == d[x2]
	assert d[x] is d[x2]
	assert d[x] != d.get('x')
	assert d[y] != d.get('y')

	x = Symbol('x')
	x2 = Symbol('x')
	assert x is x2

if __name__ == '__main__':
	test()
