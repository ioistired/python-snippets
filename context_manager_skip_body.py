#!/usr/bin/env python3

"""a failed attempt at making a context manager that skips the body of the `with` suite"""

import contextlib

class _SkipBody(Exception):
	"""Exception raised when the body of a context manager should be skipped"""

class dont_execute(contextlib.AbstractContextManager):
	def __enter__(self):
		raise _SkipBody

	def __exit__(self, typ, val, tb):
		return typ is _SkipBody

def main():
	with dont_execute():
		print('can you hear me?')

if __name__ == '__main__':
	main()
