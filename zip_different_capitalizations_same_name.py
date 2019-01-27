#!/usr/bin/env python3
# encoding: utf-8

import zipfile, itertools

def all_capitalizations(s):
	for capitalization_scheme in itertools.product((False, True), repeat=len(s)):
		yield ''.join(
				c.upper()
				if should_capitalize
				else c.lower()
			for c, should_capitalize
			in zip(s, capitalization_scheme))

with zipfile.ZipFile('eight_foos.zip', 'w') as zf:
	for capitalization in all_capitalizations('foo'):
		zf.writestr(capitalization, capitalization)

# now what happens if you extract this on a case insensitive filesystem?
