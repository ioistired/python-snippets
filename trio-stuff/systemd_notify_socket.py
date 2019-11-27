import trio
import os

async def main():
	sock = trio.socket.socket(trio.socket.AF_UNIX, trio.socket.SOCK_DGRAM)
	await sock.connect(notify_socket_address())
	# await send_all(sock, b'READY=1')
	await send_all(sock, b'STATUS=yert')
	await trio.sleep(float('inf'))

def notify_socket_address():
	addr = os.environ['NOTIFY_SOCKET']
	if addr[0] == '@':
		addr = '\0' + addr[1:]
	return addr

async def send_all(sock, data):
	total_sent = 0
	while total_sent < len(data):
		sent = await sock.send(data[total_sent:])
		if sent == 0:
			raise trio.BrokenResourceError('socket connection broken')
		total_sent += sent

if __name__ == '__main__':
	trio.run(main)
