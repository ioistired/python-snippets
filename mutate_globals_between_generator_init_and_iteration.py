#!/usr/bin/env python3

a = 0

def foo():
	yield a

g = foo()
a += 1
print(list(g))
