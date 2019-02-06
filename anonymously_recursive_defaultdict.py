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
