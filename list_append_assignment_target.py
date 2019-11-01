#!/usr/bin/env python3

class DumbList(list):
	@property
	def append(self):
		return super().append

	@append.setter
	def append(self, value):
		self.append(value)

def main():
	import time
	from timeit_ctxman_2 import timeit

	timer = timeit()
	results = DumbList()
	with timer as results.append:
		time.sleep(0.5)
		with timer as results.append:
			time.sleep(0.5)

	with timer as results.append:
		time.sleep(0.5)

	assert len(results) == 3

if __name__ == '__main__':
	main()
