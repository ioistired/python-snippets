#!/usr/bin/env python3
# encoding: utf-8

## NOTE TO SELF: just use a fucking lexer

import string

EMOTE_ALLOWED = set(string.ascii_lowercase) | set(string.ascii_uppercase) | set(string.digits)
DELIMS = set(':;')
IGNORED = {'<': '>', '`': '`'}

def parse_emote(text, i, close):
	i += 1
	current = []
	while text[i] != close:
		if text[i] not in EMOTE_ALLOWED:
			return ''

	return ''.join(current), i

def parse_emotes(text):
	parsed = []
	i = 0
	while i < len(text):
		c = text[i]
		if c in DELIMS:
			delim = c
			i += 1

			current_emote = []
			while i < len(text) and text[i] != delim:
				if text[i] not in EMOTE_ALLOWED:
					parsed.append(text[i])
					break
				current_emote.append(text[i])
				i += 1
			parsed.append('<<'+''.join(current_emote)+'>>')
		elif c in IGNORED:
			closer = IGNORED[c]
			i += 1
			while i < len(text) and text[i] != closer:
				parsed.append(text[i])
				i += 1
		else:
			parsed.append(text[i])
			i += 1

	return ''.join(parsed)
