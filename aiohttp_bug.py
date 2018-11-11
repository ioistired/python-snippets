#!/usr/bin/env python3
# encoding: utf-8

import asyncio
import os

import aiohttp

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(headers={'Authorization': os.environ['ec_token']}, loop=loop)

async def main():
	async with session.request('GET', 'https://emoji-connoisseur.python-for.life/api/v0/login') as response:
		print(response.request_info.headers['Authorization'])
		print(await response.text())

loop.run_until_complete(main())


