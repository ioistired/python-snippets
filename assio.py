#!/usr/bin/env python3

## IGNORE THIS NONSENSE

from __future__ import print_function

import inspect
import sys

try:
	import builtins
except ImportError:
	# py 2 compat for the memes
	import __builtins__
	builtins = __builtins__
	del __builtins__

if sys.version_info[0] >= 3:
	def get_frame_function_name(f):
		return f.function
else:
	def get_frame_function_name(f):
		return f[3]

def callers_function_name():
	return get_frame_function_name(inspect.stack()[2])

def print(*args, **kwargs):
	return builtins.print(callers_function_name(), *args, **kwargs)

## BUT PAY ATTENTION TO THE FOLLOWING BULLSHIT

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
		yield
		print('you\'re mum gay')

	def b():
		print(2)
		for i in range(20, 30):
			yield
			print(i)
		yield
		print(3)

	def c():
		for i in range(10, 20):
			yield
			print(i)
		print(4)
		print(5)

	loop = EventLoop()
	loop.create_task(a())
	loop.create_task(b())
	loop.create_task(c())
	loop.run()
