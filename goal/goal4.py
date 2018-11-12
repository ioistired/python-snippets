#!/usr/bin/env python3
# encoding: utf-8

class g:
	def __new__(cls, x=None):
		self = super().__new__(cls)
		self._count = 0
		return self.__call__(x)

	def __call__(self, x=None):
		if x is None:
			# no args
			self._count += 1
			return self
		else:
			return type(self).__name__ + 'o'*self._count + x


if __name__== '__main__':
	print(g()('al'))
	print(g('al'))
	print(g()()()()()('al'))
