import asyncio

from async_generator import async_generator, yield_, yield_from_

_sleep = object()

async def sleep(seconds: float):
	if not seconds:
		yield
		return
	yield _sleep, seconds

class AsyncEventLoop:
	def __init__(self):
		self.tasks = []

	def create_task(self, agen):
		self.tasks.append(agen)
		return agen

	async def run(self):
		while self.tasks:
			for task in self.tasks:
				try:
					res = await task.asend(None)
				except StopAsyncIteration:
					self.tasks.remove(task)
				else:
					if isinstance(res, tuple) and res and res[0] is _sleep:
						await asyncio.sleep(res[1])

@async_generator
async def a():
	print(0)
	await yield_from_(sleep(0))
	print(1)

@async_generator
async def b():
	print(2)
	await yield_from_(sleep(3))
	print(3)

@async_generator
async def c():
	print(4)
	await yield_from_(sleep(0))
	await yield_from_(a())
	print(5)

async def main():
	aloop = AsyncEventLoop()
	for f in a, b, c:
		aloop.create_task(f())
	await aloop.run()

if __name__ == '__main__':
	asyncio.run(main())
