#!/usr/bin/env python3
# encoding: utf-8


class Foo:
	def __init__(self):
		self._x = 1

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@x.deleter
	def x(self):
		del self._x


def main():
	x = Foo()
	print(x._x)
	print(x.x)
	x.x = 2
	print(x.x)
	del x.x
	print(x.x)


if __name__ == '__main__':
	main()
