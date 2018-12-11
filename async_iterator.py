#!/usr/bin/env python3
# encoding: utf-8

class AsyncIteratorWrapper:
	"""converts a blocking iterable to an async iterable"""
	def __init__(self, iterable):
		self.iter = iter(iterable)

	async def __anext__(self):
		try:
			return next(self.iter)
		except StopIteration as e:
			if e.value is not None:
				raise StopAsyncIteration(e.value)
			raise StopAsyncIteration

	def __aiter__(self):
		print('aiter called')
		return self

async def main():
	async for x in AsyncIteratorWrapper(range(10)):
		print(x)

if __name__ == '__main__':
	import asyncio
	asyncio.get_event_loop().run_until_complete(main())

# output: "aiter called", followed by 1–10
