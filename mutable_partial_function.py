#!/usr/bin/env python3
# encoding: utf-8

from functools import partial


def foo(t, x):
	return t[-1], x

t = list(range(5))
foo = partial(foo, t)

print('Pre  modification, foo("hi") =', foo('hi'))
t.append(5)
print('Post modification, foo("hi") =', foo('hi'))
