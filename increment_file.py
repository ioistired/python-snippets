import math

def round_up(x, base):
	return x if x % base == 0 else x + base - x % base

def increment(f):
	"""Increment the byte contents of a file-like object f
	The entire file is assumed to represent a single big-endian integer.
	An empty file represents a value of 0.
	"""
	b = f.read()
	c = int.from_bytes(b, byteorder='big')
	c += 1
	b = c.to_bytes(length=round_up(c.bit_length(), 8) // 8, byteorder='big')
	f.seek(0)
	f.write(b)
