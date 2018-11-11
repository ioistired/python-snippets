#!/usr/bin/env python3
# encoding: utf-8

import random
import os.path

from wand.image import Image

image = Image(filename=os.path.expanduser('~/Pictures/discord emoji/gentleblob.png'))

with image.clone() as liquid:
	old_size = liquid.size
	width = liquid.width
	for i in range(5):
		size = random.randint(width//2, width)
		liquid.liquid_rescale(size, size)
	liquid.liquid_rescale(*old_size)
	liquid.save(filename='gentleblob-magik.png')
