#!/usr/bin/env python3
# encoding: utf-8

import sys

def print(*values, sep=' ', end='\n', file=sys.stdout, flush=False):
	file.write(sep.join(map(str, values)))
	file.write(end)
	if flush: file.flush()

if __name__ == '__main__':
	print(1, 2, 3)
	print(4, 5, 6, end=' ', flush=True)
	print(7, 8, 9)
	print(10, 11, 12, sep='-')
