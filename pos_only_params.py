#!/usr/bin/env python3

# requires 3.8+

def f1(a=1, /):
	return a

def f2(a=1, b=2, c=3, /):
	return a, b, c

def f3(x, /, y, *, z):
	return x, y, z

print(f'{f1() = }')
print(f'{f2("a", "b") = }')
print(f'{f3("a", "b", z=1) = }')
