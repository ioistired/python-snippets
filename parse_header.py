"""
python 3.10 replacement for cgi.parse_header
"""

from email.message import EmailMessage

def parse_header(h):
	m = EmailMessage()
	m['content-type'] = h
	l = m.get_params()
	return l[0][0], dict(l[1:])
