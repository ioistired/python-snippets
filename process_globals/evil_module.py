#!/usr/bin/env python3

import builtins

def _swap_builtins(a, b):
	_a = getattr(builtins, a)
	_b = getattr(builtins, b)
	setattr(builtins, a, _b)
	setattr(builtins, b, _a)

for _a, _b in {
	'float': 'int',
	'str': 'bytes',
	'filter': 'map',
	'list': 'set',
}.items():
	_swap_builtins(_a, _b)

builtins.getattr = delattr
del builtins.__import__  # prevent future imports
