#!/usr/bin/env python3
# encoding: utf-8

import itertools

class CircularList(list):
	def __getitem__(self, x):
		if isinstance(x, slice):
			# TODO support e.g. [::-1] and [1::-1]
			if x.stop is None:  # [1:] -> all elements starting at 1 till infinity
				indices = itertools.count(x.start, x.step)
				return (self[i] for i in itertools.count(x.start, x.step))
			else:  # [5:100]
				# for [5:100] with a 
				return [self[i] for i in slice.indices(len(self) * x.step)]


