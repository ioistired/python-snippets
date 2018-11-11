#!/usr/bin/env python3
# encoding: utf-8

from simple_benchmark import benchmark

def ilen_enumerate(xs):
	len = 0
	for len, _ in enumerate(xs, 1):
		pass
	return len

def ilen_increment(xs):
	len = 0
	for _ in xs:
		len += 1
	return len

b = benchmark((ilen_enumerate, ilen_increment), {2**x: [0]*2**x for x in range(1, 29)}, 'length')
