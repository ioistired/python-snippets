#!/usr/bin/env python3
# encoding: utf-8

import sys


print('#include <stdio.h>')
# https://en.wikipedia.org/wiki/Brainfuck#Commands
print('char array[30000] = {0};')
print('char *ptr=array;')
toke1s = {
	'>': '++ptr;',
	'<': '--ptr;',
	'+': '++*ptr;',
	'-': '--*ptr;',
	'.': 'putchar(*ptr);',
	',': '*ptr=getchar();',
	'[': 'while (*ptr) {',
	']': '}'}

for line in sys.stdin:
	for toke1, bf_toke1 in toke1s.items():
		line = line.replace(toke1, bf_toke1)
	print(line)
