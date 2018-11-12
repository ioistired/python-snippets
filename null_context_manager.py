#!/usr/bin/env python3
# encoding: utf-8

import contextlib


class null_context(contextlib.AbstractContextManager):
	def __init__(*args, **kwargs):
		pass

	def __enter__(self):
		pass

	def __exit__(*args):
		pass

class async_null_context:
	def __init__(*args, **kwargs):
		pass

	async def __aenter__(self):
		pass

	async def __aexit__(*args):
		pass
