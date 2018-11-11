#!/usr/bin/env python3.6
# encoding: utf-8

def g(end=None):
	if not hasattr(g, 'out'):
		g.out = 'g'
	if not end:
		g.out += 'o'
		return g
	else:
		return g.out + end


if __name__ == '__main__':
	for result in (
		g('al'),
		g()('al'),
		g()()('al'),
		g('al')
	):
		print(result)
