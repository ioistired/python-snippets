#!/usr/bin/env python3
# encoding: utf-8

import itertools

def f(x, y):
	if x:
		return True
	elif y:
		return False
	else:
		return False

def print_table(func):
	inputs = itertools.product((True, False), repeat=2)
	for input in inputs:
		print(input, func(*input))

print_table(f)
