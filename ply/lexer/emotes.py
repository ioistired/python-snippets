#!/usr/bin/env python3
# encoding: utf-8

from ply import lex

tokens = (
	'DB_EMOTE',
	'CUSTOM_EMOTE',
	'CODE',
	'TEXT',
)

# Tokens

t_CUSTOM_EMOTE = r'<a?:\w{2,32}:\d{15,}>'
t_CODE = r'`{1,3}'
t_TEXT = '[.\n]+'

def t_DB_EMOTE(t):
	r'(:|;)([A-Za-z0-9_]{2,32})\1'

	match = lexer.lexmatch
	return match.group(2)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()
