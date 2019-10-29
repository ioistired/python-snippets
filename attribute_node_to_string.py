#!/usr/bin/env python3

import ast

def attribute_source(node):
	if type(node) is ast.Name:
		return node.id
	return attribute_source(node.value) + '.' + node.attr

def main():
	s = 'a.b.c.d.e'
	node = ast.parse(s, mode='eval').body
	assert attribute_source(node) == s

if __name__ == '__main__':
	main()
