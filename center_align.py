def center_align(text, max_length):
	to_add = max_length - len(text)
	pad = ' ' * (to_add//2)
	return ''.join([pad, text, pad])
