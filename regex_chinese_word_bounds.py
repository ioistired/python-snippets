#!/usr/bin/env python3
# encoding: utf-8

import re

zenme = re.compile(r'\b怎么\b')

without_punct = '他怎么了'
with_punct = '他「怎么」了'

if __name__ == '__main__':
	for sentence in without_punct, with_punct:
		print(sentence, zenme.search(sentence))

# this sucks
# i think they should both match, since a chinese word can end at any character
