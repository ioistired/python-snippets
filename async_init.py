#!/usr/bin/env python3
# encoding: utf-8

import asyncio
import functools
import random

def async_init(cls):
	__new__ = cls.__new__

	@functools.wraps(__new__)
	async def new(cls, *args, **kwargs):
		self = __new__(cls, *args, **kwargs)
		await self.__init__(*args, **kwargs)
		return self

	cls.__new__ = new
	return cls

@async_init
class DatabaseConnection:
	established = False

	async def __init__(self):
		# do some network IO to establish the connection
		await asyncio.sleep(random.random())
		self.established = True

async def test():
	conn = await DatabaseConnection()
	assert conn.established

if __name__ == '__main__':
	asyncio.get_event_loop().run_until_complete(test())
