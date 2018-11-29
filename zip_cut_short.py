#!/usr/bin/env python3
# encoding: utf-8

# like itertools.zip_longest, but with no fillvalue
# written for https://github.com/erikrose/more-itertools/pull/240#issuecomment-441513474

def zip(*iterables):
	iterators = list(map(iter, iterables))
	while True:
		to_yield = _build_zipped_tuple(iterators)
		if not to_yield:
			return
		yield to_yield

def _build_zipped_tuple(iterables):
	vals = []
	for iterable in iterables:
		try:
			vals.append(next(iterable))
		except StopIteration:
			break
	return tuple(vals)

if __name__ == '__main__':
	for xs in zip((1, 2, 3), (1, 2), (1,)):
		print(xs)
