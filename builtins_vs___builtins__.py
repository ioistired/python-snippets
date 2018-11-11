#!/usr/bin/env python3

import builtins

if not __debug__:
	raise AssertionError

if __name__ == '__main__':
	assert __builtins__ is builtins
else:
	assert __builtins__ is builtins.__dict__
