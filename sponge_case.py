#!/usr/bin/env python3

"""implement sPoNgEbOB mOcK cAsE using the most FP tools possible"""

import functools
import itertools
import operator

def apply(f, *args, **kwargs): return f(*args, **kwargs)

def flip(f):
	def flipped(x, y): return f(y, x)
	return flipped

def compose(*funcs):
	def composed(x): return functools.reduce(flip(apply), reversed(funcs), x)
	return composed

def sponge_case_1(s):
	return ''.join(map(apply, itertools.cycle((str.lower, str.upper)), s))

def sponge_case_2(s):
	return ''.join((str.lower, str.upper)[i % 2](c) for i, c in enumerate(s))

def sponge_case_3(s):
	return ''.join(c.upper() if p else c.lower() for p, c in zip(itertools.cycle((False, True)), s))

def sponge_case_4(s):
	# combining 2 and 3
	return ''.join((str.lower, str.upper)[p](c) for p, c in zip(itertools.cycle((False, True)), s))

def test():
	global_is_sponge_case_func = compose(
		operator.methodcaller('startswith', 'sponge_case'),
		operator.itemgetter(0))  # name, global → name
	for f in map(operator.itemgetter(-1), filter(global_is_sponge_case_func, globals().items())):
		assert f('foo bar baz') == 'fOo bAr bAz', f.__name__

if __name__ == '__main__':
	test()
