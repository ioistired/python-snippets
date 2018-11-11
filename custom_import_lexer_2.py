#!/usr/bin/env python3

from ply import lex

_SINGLE_QUOTE = "'"
_DOUBLE_QUOTE = '"'

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
	('in_short_string', 'exclusive'),
	('in_long_string', 'exclusive'),
	('in_short_bytes', 'exclusive'),
	('in_long_bytes_bytes', 'exclusive'),
)

t_SHORT_STRING = (
	        _SINGLE_QUOTE + t_SHORT_STRING_ITEM + _SINGLE_QUOTE
	+ '|' + _DOUBLE_QUOTE + t_SHORT_STRING_ITEM + _DOUBLE_QUOTE
)

t_SHORT_STRING_ITEM = r'[^\n\\]'
