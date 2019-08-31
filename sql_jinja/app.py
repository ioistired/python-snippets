#!/usr/bin/env python3

import jinja2
import jinja2.parser
from jinja2 import ext
from jinja2 import nodes

class QueryExtension(ext.Extension):
	tags = {'query', 'qblock'}

	def parse(self, parser):
		token = next(parser.stream)
		return (self._parse_query if token.value == 'query' else self._parse_qblock)(parser, token.lineno)

	def _parse_query(self, parser, lineno):
		name = parser.parse_assign_target(with_tuple=False).name
		body = parser.parse_statements(['name:endquery'], drop_needle=True)
		# name, params, defaults, body
		return nodes.Macro(name, [nodes.Name('__blocks__', 'param')], [], body).set_lineno(lineno)

	def _parse_qblock(self, parser, lineno):
		name = parser.parse_assign_target(name_only=True).name
		body = parser.parse_statements(['name:endqblock'], drop_needle=True)
		return nodes.If(
			nodes.Compare(  # test
				nodes.Const(name),
				[nodes.Operand('in', nodes.Name('__blocks__', 'load'))]),
			body,
			[],  # elif_
			[]  # orelse
		).set_lineno(lineno)

def main():
	queries = jinja2.Environment(
		loader=jinja2.FileSystemLoader('.'),
		trim_blocks=True,
		line_statement_prefix='-- :',
		extensions=[QueryExtension],
	).get_template('queries.sql').module

	class Queries:
		pass

	new_queries = Queries()

	for name, val in vars(queries).items():
		if not callable(val):
			vars(new_queries)[name] = val
			continue

		def wrapped(*blocks, _val=val):
			return _val(frozenset(blocks))

		wrapped.__name__ = name
		vars(new_queries)[name] = wrapped

	queries = new_queries

	print('---- no blocks ----')
	print(queries.users())
	print('---- login_history ----')
	print(queries.users('login_history'))
	print('---- profiles ----')
	print(queries.users('profiles'))
	print('---- all three ----')
	print(queries.users('login_history', 'profiles', 'user_id'))

if __name__ == '__main__':
	main()
