# -*- coding: utf-8 -*-

"""
jishaku.repl.compilation
~~~~~~~~~~~~~~~~~~~~~~~~

Constants, functions and classes related to classifying, compiling and executing Python code.

:copyright: (c) 2019 Devon (Gorialis) R, Io Mintz
:license: MIT, see LICENSE for more details.

"""

import ast
import inspect
import sys
import typing

import import_expression

from jishaku.functools import AsyncSender
from jishaku.repl.scope import Scope
from jishaku.repl.walkers import KeywordTransformer

REPL_CODE = """
def _repl_func(_repl_scope):
    from importlib import import_module as {0}
    try:
        pass
    finally:
        _repl_scope.update(locals())
""".format(import_expression.constants.IMPORTER)

def wrap_code(code: typing.Union[ast.Module, str]) -> ast.Module:
    """
    Compiles Python code into an async function or generator,
    and automatically adds return if the function body is a single evaluation.
    Also adds inline import expression support.
    """

    mod = ast.parse(REPL_CODE, mode='exec')
    user_code = import_expression.parse(code, mode='exec')

    definition = mod.body[-1]
    assert isinstance(definition, ast.FunctionDef)

    try_block = definition.body[-1]
    assert isinstance(try_block, ast.Try)

    try_block.body.extend(user_code.body)

    ast.fix_missing_locations(mod)

    KeywordTransformer().generic_visit(try_block)

    last_expr = try_block.body[-1]

    # if the last part isn't an expression, ignore it
    if not isinstance(last_expr, ast.Expr):
        return mod

    # if the last ex/pression is not a yield
    if not isinstance(last_expr.value, ast.Yield):
        # copy the value of the expression into a yield
        yield_stmt = ast.Yield(last_expr.value)
        ast.copy_location(yield_stmt, last_expr)
        # place the yield into its own expression
        yield_expr = ast.Expr(yield_stmt)
        ast.copy_location(yield_expr, last_expr)

        # place the yield where the original expression was
        try_block.body[-1] = yield_expr

    return mod


class ReplCodeExecutor:  # pylint: disable=too-few-public-methods
    """
    Executes/evaluates Python code inside of a function or generator.

    Example
    -------

    .. code:: python3

        total = 0

        # prints 1, 2 and 3
        async for x in ReplCodeExecutor('yield 1; yield 2; yield 3'):
            total += x
            print(x)

        # prints 6
        print(total)
    """

    def __init__(self, code: typing.Union[ast.Module, str], globals=None, locals=None):
        self.code = wrap_code(code)
        self.globals = {} if globals is None else globals
        self.locals = self.globals if locals is None else locals

    def __iter__(self):
        exec(compile(self.code, '<repl>', 'exec'), self.globals, self.locals)  # pylint: disable=exec-used
        func_def = self.locals.get('_repl_func') or self.globals['_repl_func']

        return self.traverse(func_def)

    def traverse(self, func):
        """
        Traverses an async function or generator, yielding each result.

        This function is private. The class should be used as an iterator instead of using this method.
        """
        if inspect.isgeneratorfunction(func):
            yield from func(self.locals)
        else:
            yield func(self.locals)
