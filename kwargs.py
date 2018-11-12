#!/usr/bin/env python3

def f(a, b, *, c=1):
	print(a,b,c)

f(**dict(a=1, b=2, c=3))
x = 1
print('{x}'.format(**locals()))
f(1, 2, **dict(x=0))
f(1, 2, **dict(a=3))
