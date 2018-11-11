from collections import Mapping

# https://github.com/slezica/python-frozendict/blob/7e078bf084ee734367dde8db2c8a2f00ec37375f/frozendict/__init__.py

class FrozenDict(Mapping):
	__slots__ = frozenset({'_dict', '_hash'})

	def __init__(self, *args, **kwargs):
		self._dict = dict(*args, **kwargs)
		self._hash = None

	def delete(self, key):
		new = self.__class__(self)
		del new._dict[key]
		return new

	def set(self, key, value):
		new = self.__class__(self)
		new._dict[key] = value
		return new

	def __getitem__(self, key):
		return self._dict[key]

	def __contains__(self, key):
		return key in self._dict

	def __len__(self):
		return len(self._dict)

	def __iter__(self):
		return iter(self._dict)

	def __repr__(self):
		return '{0.__class__.__name__}({0._dict!r})'.format(self)

	def __hash__(self):
		if self._hash is None:
			h = 0
			for k, v in self._dict.items():
				h ^= hash((k, v))
			self._hash = h
		return self._hash

	def copy(self):
		return self

	__copy__ = copy
