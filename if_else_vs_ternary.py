#!/usr/bin/env python3
# encoding: utf-8

import dis

print('ternary')
dis.dis('def f(): return x if y else z')

print()
print('if-else')
dis.dis("""
def f():
	if y: return x
	return z
""")

# in my CPython install, they're the same
