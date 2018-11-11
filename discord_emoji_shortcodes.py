#!/usr/bin/env python3
# encoding: utf-8

import json


with open('discord-emoji-shortcodes.json') as f:
	SHORTCODES = json.load(f)
del f

flattened_shortcodes = {}

for category, emojis in SHORTCODES.items():
	for emoji in emojis:
		flattened_shortcodes.update(dict.fromkeys(emoji['names'], emoji['surrogates']))
