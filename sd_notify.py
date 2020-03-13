import os
import socket

class Notifier:
	def __init__(self):
		self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM | socket.SOCK_NONBLOCK)
		addr = os.environ['NOTIFY_SOCKET']
		if addr[0] == '@':
			addr = '\0' + addr[1:]
		self.socket.connect(addr)

	def notify(self, state):
		self.socket.sendall(state.encode('latin1'))
