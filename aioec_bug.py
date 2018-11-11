#!/usr/bin/env python3
# encoding: utf-8

import asyncio

import aioec

loop = asyncio.get_event_loop()
client = aioec.Client(token='BNI=;6pXUYxftBItgvTAtN6X7bDGDluCnEwOnavKG9i3A4MY=', loop=loop)

loop.run_until_complete(client.login())
