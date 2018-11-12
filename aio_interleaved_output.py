#!/usr/bin/env python3
# encoding: utf-8

import asyncio

loop = asyncio.get_event_loop()

async def a():
	print('enter a')
	await asyncio.sleep(0)
	print('leave a')

async def b():
	print('enter b')
	await asyncio.sleep(0)
	print('leave b')

loop.create_task(a())
loop.run_until_complete(b())

# is the output
# enter a
# enter b
# leave a
# leave b
# ?

# yes
