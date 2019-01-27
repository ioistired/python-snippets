#!/usr/bin/env python3

import builtins
import dis

# capture the generated internal class function whenever a new class is built

old_build_class = __build_class__
class_funcs = []

def __build_class__(func, *args, **kwargs):
	class_funcs.append(func)
	return old_build_class(func, *args, **kwargs)

builtins.__build_class__ = __build_class__

# let's build a class to see how it works

class Foo:
	x = 1

foo = class_funcs[-1]  # the function corresponding to Foo
print(foo)
dis.dis(foo)

# the bytecode:
#  0 LOAD_NAME        0 (__name__)
#  2 STORE_NAME       1 (__module__)
#  4 LOAD_CONST       0 ('Foo')
#  6 STORE_NAME       2 (__qualname__)
#
#  8 LOAD_CONST       1 (1)
# 10 STORE_NAME       3 (x)
# 12 LOAD_CONST       2 (None)
# 14 RETURN_VALUE

# hm, these are global assignments.

def closure():
	def inner():
		foo()
	inner()
closure()

assert 'x' in globals()
assert x == 1
