#!/usr/bin/env python3

import wand.image
import wand.color
import wand.drawing
from wand.display import display
import sys

# padding from the page to the post background
POST_PADDING = 20
# padding from the post background to the image
IMAGE_PADDING = 30
PAGE_BACKGROUND_COLOR = wand.color.Color('#191b22')
POST_BACKGROUND_COLOR = wand.color.Color('#313543')

def draw_background(img, *, color, left, top, right, bottom):
	with wand.drawing.Drawing() as bg:
		bg.fill_color = color
		bg.rectangle(left=left, top=top, right=right, bottom=bottom)
		bg(img)

def main():
	with (
		wand.image.Image(filename='thisyouradmin1.png') as this_your_admin,
		wand.image.Image(filename='thisyouradmin2.png') as you_clowns,
		wand.image.Image(blob=sys.stdin.buffer.read()) as to_insert,
	):
		target_width = this_your_admin.width - 2 * POST_PADDING - 2 * IMAGE_PADDING
		to_insert.transform(resize=f'{target_width}x{to_insert.height}')

		# lol i don't wanna indent for another context manager
		out = wand.image.Image(
			width=this_your_admin.width,
			height=this_your_admin.height + to_insert.height + you_clowns.height,
		)
		out.composite(this_your_admin, 0, 0)

		draw_background(
			out, color=PAGE_BACKGROUND_COLOR,
			left=0, top=this_your_admin.height,
			right=out.width, bottom=this_your_admin.height+to_insert.height,
		)

		draw_background(
			out, color=POST_BACKGROUND_COLOR,
			left=POST_PADDING, top=this_your_admin.height,
			right=out.width-POST_PADDING, bottom=this_your_admin.height+to_insert.height,
		)

		out.composite(to_insert, POST_PADDING + IMAGE_PADDING, this_your_admin.height)
		out.composite(you_clowns, 0, this_your_admin.height + to_insert.height)
		with out.convert('png') as out:
			out.save(file=sys.stdout.buffer)
			display(out)

if __name__ == '__main__':
	main()
