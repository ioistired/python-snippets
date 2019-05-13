from typing import Callable

def bit_range_mask(*args):
	lo, hi = _parse_range_args(*args)

	if lo == 0:
		return (1 << hi) - 1

	return ((1 << hi) - 1) & ~((1 << lo) - 1)

def bit_range(*args) -> typing.Callable[[int], int]:
	lo, hi = _parse_range_args(*args)
	mask = bit_range_mask(lo, hi)

	if lo == 0:
		return lambda x: x & mask
	return lambda x: (x & mask) >> lo

def _parse_range_args(*args):
	r = range(*args)
	if r.step != 1: raise NotImplementedError('use a step of 1')
	if r.start >= r.stop: raise ValueError('lower bound must be < upper bound')
	return r.start, r.stop
