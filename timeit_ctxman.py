#!/usr/bin/env python3

import contextlib
import time

class timeit(contextlib.AbstractContextManager):
	def __enter__(self):
		self.start = time.perf_counter()
		return self

	def __exit__(self, *excinfo):
		self.end = time.perf_counter()
		self.time = self.end - self.start

def test():
	import math

	with contextlib.suppress(ValueError):
		with timeit() as timer:
			time.sleep(2)
			raise ValueError

	assert math.floor(timer.time) == 2

if __name__ == '__main__':
	test()
