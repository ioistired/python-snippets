#!/usr/bin/env python3

class cm:
	def __enter__(self):
		pass
	def __exit__(self, tp, val, tb):
		print(tp)
		return True

def main():
	import sys
	with cm():
		sys.exit(1)

if __name__ == '__main__':
	main()
