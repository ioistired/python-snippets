#!/usr/bin/env python3

import ast
import inspect

def i18n_docstring(func):
	src = inspect.getsource(func)
	try:
		tree = ast.parse(src)
	except IndentationError:
		# this works regardless of how indented the function is
		# because python does not care about how wide an indentation is, as long as it is consistent
		tree = ast.parse('class IndentFix:\n' + src)
		tree = tree.body[0].body[0]  # ClassDef -> FunctionDef
	else:
		tree = tree.body[0]  # FunctionDef

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
	return func

def id(x): return x

@i18n_docstring
@id  # make sure it works with decos
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

class Quux:
	@i18n_docstring
	@id
	def garply(self):
		_("""hi

		bye
		""")
		return 0

_ = id

@i18n_docstring
class Waldo:
	_('hi')

def fred():
	@i18n_docstring
	def fred():
		_('hi sorry ran out of names here')
		return fred
	return fred

def test():
	assert foo.__doc__.startswith('do a thing')
	assert bar.__doc__ is None
	assert baz.__doc__.startswith('frobnicate')
	assert Quux.garply.__doc__.startswith('hi')
	assert Waldo.__doc__ == 'hi'
	assert fred().__doc__.startswith('hi')

if __name__ == '__main__':
	test()
