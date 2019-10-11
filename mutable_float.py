import ctypes
import sys

SIZEOF_PYOBJECT = sys.getsizeof(object())

class MutableFloat(float):
	def set(self, val):
		ob_fval = ctypes.c_double.from_address(id(self) + SIZEOF_PYOBJECT)
		ob_fval.value = val
