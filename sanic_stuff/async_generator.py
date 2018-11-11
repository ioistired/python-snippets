#!/usr/bin/env python3.6

import asyncio

from sanic import Sanic
from sanic.response import text

app = Sanic()


@app.route('/gen')
async def gen(request):
	for i in range(10):
		yield str(i)
		await asyncio.sleep(1)


if __name__ == '__main__':
	app.run(host='localhost', port=8000)
