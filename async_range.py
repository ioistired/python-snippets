#!/usr/bin/env python3
# encoding: utf-8

class AsyncRange:
	__slots__ = frozenset({'start', 'stop', 'step'})

	def __new__(cls, *args):
		self = super().__new__(cls)
		# use builtins.range to parse the args, as range() args are a bit complex
		r = range(*args)
		self.start, self.stop, self.step = r.start, r.stop, r.step

		return self

	# TODO define __getitem__ and stuff, but that's outside the scope of this snippet

	async def __aiter__(self):
		i = self.start
		remaining = (self.stop - self.start) // self.step

		while remaining:
			yield i
			i += self.step
			remaining -= 1

		# below line is only for __anext__, my bad
		# raise StopAsyncIteration

async def test():
	xs = [x async for x in AsyncRange(10, 100, 2)]
	assert xs == list(range(10, 100, 2)), xs

if __name__ == '__main__':
	import asyncio
	asyncio.get_event_loop().run_until_complete(test())
