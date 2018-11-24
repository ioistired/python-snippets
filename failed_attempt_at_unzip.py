#!/usr/bin/env python3
# encoding: utf-8

from more_itertools import peekable, consumer

def unzip(iterable):
	iterable = peekable(iterable)
	len_head = len(iterable.peek())

	@consumer
	def gen(i, last=False):
		while True:
			yield iterable.peek()[i]
			if last:
				next(iterable)

	gens = [gen(i) for i in range(len_head - 1)]
	gens.append(gen(len_head - 1, last=True))

	return gens
