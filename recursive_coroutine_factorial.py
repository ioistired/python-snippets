#!/usr/bin/env python3
# encoding: utf-8

async def factorial(n, _acc=1):
	if n < 2:
		return _acc
	else:
		return await factorial(n-1, n*_acc)


if __name__ == '__main__':
	import sys

	try:
		n = int(sys.argv[1])
	except IndexError:
		raise TypeError('first argument must be an integer')

	print(factorial(n).send(None))
