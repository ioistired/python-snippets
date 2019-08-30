#!/usr/bin/env python3

import jinja2
import jinja2.parser
from jinja2 import ext
from jinja2 import nodes

del jinja2.parser.Parser.parse_block
jinja2.parser._statement_keywords -= {'block'}

class QueryExtension(ext.Extension):
	tags = {'query'}

	def parse(self, parser):
		lineno = next(parser.stream).lineno
		name = parser.parse_assign_target(with_tuple=False).name
		body = parser.parse_statements(['name:endquery'], drop_needle=True)
		# name, params, defaults, body
		return nodes.Macro(name, [nodes.Name('__blocks__', 'param')], [], body).set_lineno(lineno)

class QueryBlockExtension(jinja2.ext.Extension):
	tags = {'block'}

	def parse(self, parser):
		lineno = next(parser.stream).lineno
		name = parser.parse_assign_target(name_only=True).name
		body = parser.parse_statements(['name:endblock'], drop_needle=True)
		return nodes.If(
			nodes.Compare(  # test
				nodes.Const(name),
				[nodes.Operand('in', nodes.Name('__blocks__', 'load'))]),
			body,
			[],  # elif_
			[])  # orelse

queries = jinja2.Environment(
	loader=jinja2.FileSystemLoader('.'),
	trim_blocks=True,
	line_statement_prefix='-- :',
	extensions=[QueryExtension, QueryBlockExtension],
).get_template('queries.sql').module

print(queries.users)
print(queries.users())
print('---- login_history ----')
print(queries.users({'login_history'}))
print('---- profiles ----')
print(queries.users({'profiles'}))
print('---- all three ----')
print(queries.users({'login_history', 'profiles', 'user_id'}))
