#!/usr/bin/env python3

from ply import lex

tokens = (
	'IMPORT_EXPRESSION_START',
	'IMPORT_EXPRESSION_END',


	'STRING_OR_BYTES_LITERAL',
	'STRING_LITERAL',
	'BYTES_LITERAL',

	'STRING_PREFIX',
	'SHORT_STRING',
	'LONG_STRING',

	'SHORT_STRING_ITEM',
	'LONG_STRING_ITEM',

	'SHORT_STRING_CHAR',
	'LONG_STRING_CHAR',
	'STRING_ESCAPE_SEQ',


	'BYTES_PREFIX',
	'SHORT_BYTES',
	'LONG_BYTES'

	'SHORT_BYTES_ITEM',
	'LONG_BYTES_ITEM',

	'SHORT_BYTES_CHAR',
	'LONG_BYTES_CHAR',
	'BYTES_ESCAPE_SEQ',
)

states = (
	('in_short_string_single_quote', 'exclusive'),
	('in_short_string_double_quote', 'exclusive'),
	('in_long_string_single_quote', 'exclusive'),
	('in_long_string_double_quote', 'exclusive'),
	('in_short_bytes_single_quote', 'exclusive'),
	('in_long_bytes_double_quote', 'exclusive'),
)

def t_SHORT_STRING(t):
	r"""["|']"""
	quote_type = {"'": 'single', '"': 'double'}[t.value]
	t.lexer.begin(f'in_short_string_{quote_type}_quote')

t_STRING_PREFIX = '(?i)r|u|f|fr|rf'

def t_SHORT_STRING_CHAR(t):
	r'[^\n\\]'
	current_quote = {'in_short_string_single_quote': "'", 'in_short_string_double_quote': '"'}[t.lexer.state]
	if t.value == current_quote:
		t.lexer.pop_state()

