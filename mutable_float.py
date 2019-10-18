import ctypes
import operator
import sys

SIZEOF_PYOBJECT = sys.getsizeof(object())

class MutableFloat(float):
	def set(self, val):
		ob_fval = ctypes.c_double.from_address(id(self) + SIZEOF_PYOBJECT)
		ob_fval.value = val

	for op in operator.add, operator.sub, operator.mul, operator.truediv, operator.floordiv, operator.pow:
		def meth(self, other, *, _op=op):
			self.set(_op(self, other))
			return self  # why tho
		vars()[f'__i{op.__name__}__'] = meth

	del op, meth
