#!/usr/bin/env python3
# encoding: utf-8

from collections import OrderedDict


class LRUDict(OrderedDict):
	def __init__(self, limit):
		self.limit = limit

	def __getitem__(self, key):
		self.move_to_end(key)
		return super().__getitem__(key)

	def __setitem__(self, key, value):
		super().__setitem__(key, value)
		if len(self) > self.limit:
			self.popitem(last=False)
