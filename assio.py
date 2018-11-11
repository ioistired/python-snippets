#!/usr/bin/env python3

from __future__ import print_function

class EventLoop:
	def __init__(self):
		self.tasks = []

	def create_task(self, task):
		self.tasks.append(task)

	def run(self):
		while self.tasks:
			for task in self.tasks:
				try:
					next(task)
				except StopIteration:
					self.tasks.remove(task)

if __name__ == '__main__':
	def a():
		print(0)
		x = yield from b()
		print(x)

	def b():
		print(2)
		yield
		c()
		print(3)
		return 6

	def c():
		print(4)
		print(5)

	loop = EventLoop()
	loop.create_task(a())
	loop.create_task(b())
	loop.run()

