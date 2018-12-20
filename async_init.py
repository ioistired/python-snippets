#!/usr/bin/env python3
# encoding: utf-8

def AsyncInit(name, bases, attrs):
	cls = type(name, bases, attrs)

	async def __new__(cls, *args, **kwargs):
		self = object.__new__(cls)
		await self.__init__(*args, **kwargs)
		return self

	cls.__new__ = __new__
	return cls

class Foo(metaclass=AsyncInit):
	async def __init__(self):
		self.x = 1

async def test():
	x = await Foo()
	assert x.x == 1

if __name__ == '__main__':
	import asyncio
	asyncio.get_event_loop().run_until_complete(test())
