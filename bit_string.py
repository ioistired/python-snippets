#!/usr/bin/env python3
# encoding: utf-8

import collections.abc
import math
import operator

def bit_length(x: int):
	if x == 0:
		# log2(0) is undefined
		return 1
	return int(math.log2(x) + 1)

def _validate_cls_args(value, size):
	if value < 0:
		raise ValueError('value must be non-negative')

	if size < 1:
		raise ValueError('size must be positive')

	if bit_length(value) > size:
		raise ValueError(f'value must have at most {size} bits')

class BitString(collections.abc.Sequence):
	def __new__(cls, value=0, *, size):
		self = super().__new__(cls)

		_validate_cls_args(value, size)

		self.value = value
		self.size = size

		return self

	def __getitem__(self, index):
		"""0 is MSB. index must be in range(self.size)"""
		index = self._normalize_index(index)

		return (self.value >> (self.size - index - 1)) & 1

	def __add__(self, other: 'BitString'):
		"""concatenate self with another bitstring or integer"""
		return type(self)(
			value=(self.value << len(other)) | other.value,
			size=self.size + other.size)

	def _normalize_index(self, index):
		"""wrap negative indices"""
		index = operator.index(index)

		if index < 0:
			index += self.size

		if index not in range(self.size):
			raise IndexError

		return index

	def __len__(self):
		return self.size

	def __int__(self):
		return self.value

	__index__ = __int__

class MutableBitString(ReadOnlyBitString, collections.abc.MutableSequence):
	def __init__(self, value=0, *, size):
		_validate_cls_args(value, size)

		self.value = value
		self.size = size

	def __setitem__(self, index, value: int):
		if not isinstance(value, int) or value not in (0, 1):
			raise TypeError('new value must be a binary integer')
		index = self._normalize_index(index)

		# suppose i = 4 and size = 7
		# mask = 0001000
		mask = 1 << (self.size - index - 1)

		if value == 0:
			# e.g. x & 1110111
			# preserves all bits except index 4, which is set to 0
			self.value &= ~mask
		else:
			# e.g. x | 0001000
			# sets index 4 to 1
			self.value |= mask

	def insert(self, index, value):
		raise TypeError('inserting bits is not supported')

	def __delitem__(self, index):
		raise TypeError('deleting individual bits is not supported')
