#!/usr/bin/env python3

import contextlib
import time

from mutable_float import MutableFloat

class timeit(contextlib.AbstractContextManager):
	"""re-entrant context manager that times execution of its body."""

	def __init__(self):
		self.times = []

	def __enter__(self, *, _timer=time.perf_counter):
		elapsed = MutableFloat('nan')
		self.times.append((elapsed, _timer()))
		return elapsed

	def __exit__(self, *excinfo, _timer=time.perf_counter):
		t1 = time.perf_counter()
		elapsed, t0 = self.times.pop()
		elapsed.set(t1 - t0)

def test():
	timer = timeit()
	with timer as elapsed1:
		time.sleep(1/2)
		with timer as elapsed2:
			time.sleep(1/2)
		time.sleep(1/2)

	assert int(elapsed1) == 1
	assert round(elapsed2, 1) == 0.5

if __name__ == '__main__':
	test()
