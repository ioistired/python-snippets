#!/usr/bin/env python3

import ast
import inspect

def i18n_docstring(func):
	src = inspect.getsource(func)
	orig_tree = ast.parse(src)
	tree = orig_tree.body[0]  # the FunctionDef

	if not isinstance(tree.body[0], ast.Expr):
		return func

	tree = tree.body[0].value
	if not isinstance(tree, ast.Call):
		return func

	if not isinstance(tree.func, ast.Name) or tree.func.id != '_':
		return func

	assert len(tree.args) == 1
	assert isinstance(tree.args[0], ast.Str)

	func.__doc__ = tree.args[0].s
	orig_tree.body[0] = ast.Pass()
	return func

@i18n_docstring
def foo():
	_("""do a thing

	in case the thing is not doable, do another thing
	""")

	return 1

@i18n_docstring
def bar():
	return 2

@i18n_docstring
def baz():
	"""frobnicate the quux machine"""
	return 3

def test():
	assert foo.__doc__.startswith('do a thing')
	assert bar.__doc__ is None
	assert baz.__doc__.startswith('frobnicate')

if __name__ == '__main__':
	test()
