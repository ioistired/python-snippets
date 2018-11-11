import asyncio


# TingPing1 async functions don't make sense for most things
# TingPing1 like when an event happens [and] the callback was async[,]
# hexchat wouldn't print it until the async function finished

async def slep():
	print('before slep')
	await asyncio.sleep(1)
	print('after slep')


asyncio.get_event_loop().run_until_complete(slep())
