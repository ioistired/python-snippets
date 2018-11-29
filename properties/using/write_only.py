#!/usr/bin/env python3
# encoding: ascii

import hashlib


def hash(password: str):
	return hashlib.sha256(password.encode('utf-8')).digest()


class User:
	def __init__(self, name, password):
		self.name = name
		self.password = password

	@property
	def password(self):
		raise AttributeError('cannot read password')

	@password.setter
	def password(self, new: str):
		self.password_hash = hash(new)

	@password.deleter
	def password(self):
		self.password_hash = None

	def validate_password(self, password: str):
		if self.password_hash is None:
			return False

		return hash(password) == self.password_hash


if __name__ == '__main__':
	import sys
	import getpass

	user = User(
		input('Username? '),
		getpass.getpass('Password? ')
	)

	try:
		print(user.password)
	except AttributeError:
		print("can't get password!")

	print('Password hash:', user.password_hash)

	if user.validate_password(getpass.getpass('Confirm password: ')):
		print('Password matches!')
	else:
		print('Wrong password.')
		sys.exit(1)
