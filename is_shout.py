#!/usr/bin/env python3
# encoding: utf-8

import sys
from unicodedata import category as unicode_category

UPPERCASE_LETTERS = set()
for c in map(chr, range(sys.maxunicode+1)):
	if unicode_category(c) == 'Lu':
		UPPERCASE_LETTERS.add(c)
UPPERCASE_LETTERS = frozenset(UPPERCASE_LETTERS)
del c

def is_shout_0(str):
	sum = 0
	for c in str:
		sum += c in UPPERCASE_LETTERS
	return sum / len(str)

def is_shout_1(str):
	sum = 0
	for c in str:
		sum += unicode_category(c) == 'Lu'
	return sum / len(str)

# fastest
def is_shout_2(str):
	sum = 0
	for c in str:
		if c in UPPERCASE_LETTERS:
			sum += 1
	return sum / len(str)

def is_shout_3(str):
	sum = 0
	for c in str:
		if unicode_category(c) == 'Lu':
			sum += 1
	return sum / len(str)
