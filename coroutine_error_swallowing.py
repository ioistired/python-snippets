#!/usr/bin/env python3
# encoding: utf-8

async def error():
	raise Exception

def thing():
	return error()

async def ag_error():
	yield 1
	raise Exception

def ag_thing():
	return ag_error()

async def main():
	import traceback

	try:
		await thing()  # thing won't be in the traceback
	except:
		traceback.print_exc()

	try:
		async for x in ag_thing():  # ag_thing won't be in the traceback
			pass
	except:
		traceback.print_exc()

if __name__ == '__main__':
	import asyncio
	asyncio.get_event_loop().run_until_complete(main())
