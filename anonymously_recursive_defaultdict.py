#!/usr/bin/env python3
# encoding: utf-8

from collections import defaultdict

# behold: the recursive defaultdict!
def a():
	return defaultdict(a)

d = a()
# this enables such wild shit as
assert d[1][2][3] == {}
d[1][2] = 3
# it generates dicts on the fly!
assert d[1] == {2: 3}

# but can we do it without named recursion?

(lambda f: f(f))(lambda f: lambda: defaultdict(f))
# doesn't work (missing required positional argument f)

Z = lambda f: (lambda x: x(x))(lambda y: f(lambda v: y(y)(v)))
# we use a modified version of Z that works on a zero argument function
Z = lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))

a = Z(lambda f: lambda: defaultdict(f))
d = a()
assert d[1][2][3] == {}
d[1][2] = 3
assert d[1] == {2: 3}
