import base64

def b64decode(s, *args, **kwargs):
	"""like base64.b64decode but doesn't require padding at the end"""
	missing_padding = len(s) % 4
	if missing_padding:
		s += b'=' * (4 - missing_padding)
	return base64.b64decode(s, *args, **kwargs)
