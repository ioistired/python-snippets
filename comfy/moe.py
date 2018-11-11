import aiofiles
import aiohttp
import requests

session = requests.Session()


async def get_session():
	"""avoids "ClientSession created outside of coroutine" :^)"""
	global aio_session
	aio_session = aiohttp.ClientSession()


async def upload_file(selected_file):
	await get_session()
	async with aiofiles.open(selected_file, mode='r') as f:
		payload = {"files[]": await f.read()}
	async with aio_session.post(url="https://comfy.moe/upload.php", data=payload) as r:
		json = await r.json()
		return json


def upload_file_sync(selected_file):
	try:
		with open(selected_file, 'r') as f:
			response = session.post(
				url="https://comfy.moe/upload.php",
				files={"files[]": f.read()}
		response = response.json()
		print(response)
		return [file['url'] for file in response['files']]
	except requests.exceptions.ConnectionError:
		print("Upload to https://comfy.moe/ failed")
