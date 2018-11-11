add_method = lambda self, other: self * other

class AdditionMultiplies:
	def __add__(self, other):
		return self * other


class ExtendsStr((lambda: input())(), metaclass=AdditionMultiplies):
	pass


class ExtendsInt((lambda: 1)(), metaclass=AdditionMultiplies):
	pass