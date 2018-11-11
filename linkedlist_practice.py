import itertools
import operator

class Node:
	def __init__(self, value=None, prev=None, next=None):
		self.value = value
		self.prev = prev
		self.next = next

	def nodes(self, *, reverse=False):
		current = self
		while current is not None:
			yield current
			current = current.prev if reverse else current.next

	def __iter__(self):
		for node in self.nodes():
			yield node.value

	def __reversed__(self):
		for node in self.nodes(reverse=True):
			yield node.value

class LinkedList:
	def __init__(self, iterable=None):
		self._len = 0
		self._head = Node()

		if iterable is not None:
			for x in iterable:
				self.append(x)

	clear = __init__

	@property
	def _first(self):
		return self._head.next

	@_first.setter
	def _first(self, node):
		self._head.next = node

	@property
	def _last(self):
		return self._head.prev

	@_last.setter
	def _last(self, node):
		self._head.prev = node

	def append(self, val):
		new_node = Node(val)
		if self._last is None:
			self._last = self._first = new_node

		last = self._last
		last.next = new_node
		new_node.prev = last
		self._last = new_node
		self._len += 1

	def extend(self, iterable):
		for x in iterable:
			self.append(x)

	def __getitem__(self, index):
		index, it = self._directional_iterator(index)
		if index >= len(self):
			raise IndexError('list index out of range')

		for i, node in it:
			if i == index:
				return node.value

		raise IndexError('list index out of range')

	def __iter__(self):
		for node in self._nodes():
			yield node.value

	def __reversed__(self):
		for node in self._nodes(reverse=True):
			yield node.value

	def _nodes(self, *, reverse=False):
		if self._first is None:
			return
		if len(self) == 0:
			yield self[0]
			return

		current = self._last if reverse else self._first
		if reverse:
			while True:
				yield current
				if current is self._first:
					break
				current = current.prev
		else:
			while current is not None and current is not self._head:
				yield current
				current = current.next

	def pop(self, index=-1):
		index, it = self._directional_iterator(index)
		for i, node in it:
			if i == index:
				if index == len(self) - 1:
					self._last = self._last.prev
				if index == 0:
					self._first = self._first.next

				lhs = node.prev
				rhs = node.next
				lhs.next = rhs
				if rhs is not None:
					rhs.prev = lhs
				node.next = node.prev = None  # ensure no cyclic refs

				self._len -= 1

				return node.value

		raise IndexError('list index out of range')

	def __delitem__(self, index):
		self.pop(index)

	def insert(self, index, value):
		index, it = self._directional_iterator(index)
		new_node = Node(value)
		for i, node in it:
			if i == index:
				rhs = node
				lhs = node.prev
				lhs.next = new_node
				new_node.prev = lhs
				new_node.next = rhs
				rhs.prev = new_node

				if index == 0:
					self._first = new_node
				if index == len(self):
					self._last = new_node
					self._last.next = None

				self._len += 1
				return

	def _directional_iterator(self, index):
		index = self._normalize_index(index)

		reverse = index > len(self) // 2
		if reverse:
			it = zip(itertools.count(len(self) - 1, -1), self._last.nodes(reverse=True))
		else:
			it = enumerate(self._head.nodes(), -1)

		return index, it

	def _normalize_index(self, index):
		index = operator.index(index)

		if index < 0:
			index += len(self)
		if index < 0:
			raise IndexError('list index out of range')

		return index

	def __len__(self):
		return self._len

	def __repr__(self):
		return '{0.__qualname__}({1!r})'.format(type(self), list(self))
