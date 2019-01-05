#!/usr/bin/env python3

import builtins
import dis

old_build_class = __build_class__
class_funcs = []

def __build_class__(func, *args, **kwargs):
	class_funcs.append(func)
	return old_build_class(func, *args, **kwargs)

builtins.__build_class__ = __build_class__

class Foo: x = 1

foo = class_funcs[0]
print(foo)
dis.dis(foo)

foo()
assert x == 1
