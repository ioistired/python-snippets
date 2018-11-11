#!/usr/bin/env python3
# encoding: utf-8

import contextlib


def subclasses(cls):
	yield cls

	def aux(cls):
		with contextlib.suppress(TypeError):
			for cls in cls.__subclasses__():
				yield cls
				yield from aux(cls)

	yield from aux(cls)
