#!/usr/bin/env python3
# encoding: utf-8

import sys
import time


def brailles():
	return map(chr, range(0x2800, 0x2900))

def print_in_place(iterable, delay=0.1):
	for string in iterable:
		print(string, end='')
		time.sleep(delay)
		print('\b', end='')  # backspace
		# print without newline does not
		# flush by default
		sys.stdout.flush()
	# we need a newline at the end
	print()


if __name__ == '__main__':
	print_in_place(brailles(), 15/256)
