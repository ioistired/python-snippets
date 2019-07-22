#!/usr/bin/env python3

from io import BytesIO

from PIL import Image, ImageSequence

def frame_count(data):
	with Image.open(data) as im:
		return sum(1 for _ in ImageSequence.Iterator(im))

if __name__ == '__main__':
	import sys
	print(frame_count(sys.stdin.detach()))
