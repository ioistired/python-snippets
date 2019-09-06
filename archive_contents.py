#!/usr/bin/env python3

import tarfile
import typing.io
import zipfile

def archive_contents(archive: typing.io.BinaryIO):
	try:
		with tarfile.open(fileobj=archive) as tar:
			return tar.getnames()
	except tarfile.ReadError:
		pass

	try:
		with zipfile.ZipFile(archive) as zip:
			return zip.namelist()
	except zipfile.BadZipFile:
		raise ValueError('Not a tar or zip file')

def main():
	import sys
	for f in archive_contents(sys.stdin.buffer):
		print(f)

if __name__ == '__main__':
	main()
