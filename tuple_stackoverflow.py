#!/usr/bin/env python3
# encoding: utf-8

import sys

x = ()
y = ()
for _ in range(sys.getrecursionlimit()):
	x = (x,)
	y = (y,)

if __name__ == '__main__':
	x == y
