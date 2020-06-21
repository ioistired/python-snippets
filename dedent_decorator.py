#!/usr/bin/env python3

import textwrap

def dedent_all(f):
	"""Dedents all constant strings in the decorated function.
	DO NOT use this with functions containing f-strings.
	"""
	consts = list(f.__code__.co_consts)
	for i, const in enumerate(consts):
		if type(const) is str:
			consts[i] = textwrap.dedent(const)
	f.__code__ = f.__code__.replace(co_consts=tuple(consts))
	return f

@dedent_all
def foo():
	return """
	hi
	there
	"""

if __name__ == '__main__':
	assert foo() == '\nhi\nthere\n'
