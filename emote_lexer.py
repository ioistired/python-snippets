#!/usr/bin/env python3
# encoding: utf-8

import asyncio

import ply.lex

tokens = (
	"CODE",
	"ESCAPED_EMOTE",
	"CUSTOM_EMOTE",
	"EMOTE",
	"TEXT",
)

"""Matches code blocks, which should be ignored."""
t_CODE = '(?su)(?P<code>`{1,3}).+?(?P=code)'

"""Matches \:foo: and \;foo;, allowing one to prevent the emote auto response for one emote."""
# we don't need to match :foo\:, since "foo\" is not a valid emote name anyway
t_ESCAPED_EMOTE = r'(?a)\\(?P<colon>:|;)\w{2,32}(?P=colon)'

"""Matches only custom server emotes."""
t_CUSTOM_EMOTE = r'(?a)<(?P<animated>a?):(?P<name>\w{2,32}):(?P<id>\d{17,})>'

"""Matches :foo: and ;foo; but not :foo;. Used for emotes in text."""
t_EMOTE = r'(?a)(?P<colon>:|;)(?P<name>\w{2,32})(?P=colon)'

t_TEXT = r'(?s).+?'

def t_error(t):
	raise SyntaxError(f'Unknown text "{t.value}"')

ply.lex.lex()

def main():
	import textwrap

	test = textwrap.dedent("""
		You're mom gay
		haha lol xd
		:hahaYes: :gwchadthink: ;gwchadthink;
		\:gwchadthink: `:gwchadthink:`
		```
		:gwchadthink:
		` foo bar
		```
	""")
	ply.lex.input(test)

	print(test)

	for toke1 in iter(ply.lex.token, None):
		print(repr(toke1.type), repr(toke1.value))

	ply.lex.runmain()

if __name__ == '__main__':
	main()
