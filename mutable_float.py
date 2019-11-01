import ctypes
import operator
import sys

SIZEOF_PYOBJECT = sys.getsizeof(object())

class MutableFloat(float):
	"""
	Implementation of a mutable float.
	CPython only. May create nasal dragons.
	"""

	def set(self, val):
		ob_fval = ctypes.c_double.from_address(id(self) + SIZEOF_PYOBJECT)
		ob_fval.value = val

	for op in (
		operator.add, operator.sub, operator.mul, operator.matmul, operator.truediv, operator.floordiv, operator.pow,
		operator.mod, pow, operator.lshift, operator.rshift, operator.and_, operator.xor, oeprator.or_,
	):
		def meth(self, other, *, _op=op):
			self.set(_op(self, other))
			return self  # why tho
		vars()[f'__i{op.__name__.strip("_")}__'] = meth

	del op, meth

	__hash__ = None
