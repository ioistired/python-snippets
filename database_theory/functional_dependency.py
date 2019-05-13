class FunctionalDependency:
	def __init__(self, lhs, rhs):
		self.lhs = frozenset(lhs)
		self.rhs = frozenset(rhs)

	def __hash__(self):
		return hash((type(self), self.lhs, self.rhs))

	def __eq__(self, other):
		return self is other or (isinstance(other, type(self)) and self.lhs == other.lhs and self.rhs == other.rhs)

	def __repr__(self):
		return f'{type(self).__name__}({self.lhs}, {self.rhs})'

	def __str__(self):
		return f'{" ".join(self.lhs)} → {" ".join(self.rhs)}'
