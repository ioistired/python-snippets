# google interview, 2018-11-07
# https://docs.google.com/document/d/1StD1BfIqLckiNZ3gDQ0KtOLQO3InbmDm4cF24N07mzY/edit

class Tree:
	__slots__ = ('left', 'value', 'right')

	def __init__(self):
		self.value = None
		self.left = None
		self.right = None

	def add(self, x):
		if self.value is None:
			self.value = x
			return

		def _aux(attr):
			if getattr(self, attr) is None:
				setattr(self, attr, type(self)())
				setattr(getattr(self, attr), 'value', x)
				return
			getattr(self, attr).add(x)

		if x > self.value:
			_aux('right')
		else:
			_aux('left')

	def __contains__(self, x):
		if self.value is None:
			return False
		if self.value == x:
			return True

		# recursive case
		if x > self.value:
			if self.right is None: return False
			return x in self.right

		if self.left is None: return False
		return x in self.left

	def print_in_order(self):
		if self.left is not None:
			self.left.print_in_order()
		if self.value is not None:
			print(self.value)
		if self.right is not None:
			self.right.print_in_order()

	def remove(self, x):
		def aux(tree):
			if tree is None:
				return None

			if tree.left is tree.right is None:
				return None

			if x > tree.value:
				tree.right = aux(tree.right)
				return tree
			if x < tree.value:
				tree.left = aux(tree.left)
				return tree

			# x == tree.value
			# 1 child node
			# in case of 2 child nodes, insert tree.right at tree.left.right.right...., return tree.left
			return tree.left or tree.right

		if aux(self) is None:
			self.value = None
