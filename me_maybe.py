#!/usr/bin/env python3
# encoding: utf-8

import os.path

from wand.image import Image
from wand.display import display

class What:
	def __call__(self, *args, **kwargs):
		display(Image(filename=os.path.expanduser('~/Pictures/memes?/my-number-iphone.png')))
