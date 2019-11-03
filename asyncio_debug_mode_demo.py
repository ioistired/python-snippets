#!/usr/bin/env python3

import asyncio
import time

async def a():
	time.sleep(0.5)
	return await asyncio.sleep(0, 'aw shit')

async def b():
	return await asyncio.sleep(0, 'oh fuck')

def main():
	loop = asyncio.new_event_loop()
	loop.set_debug(True)

	loop.create_task(a())
	loop.create_task(b())

	loop.run_forever()

if __name__ == '__main__':
	main()
