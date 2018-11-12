#!/usr/bin/env python3
# encoding: utf-8

import sys


print('#include <stdio.h>')
# https://en.wikipedia.org/wiki/Brainfuck#Commands
print('char array[30000] = {0};')
print('char *ptr=array;')
print('int main(void) {')
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
	for char in line:
		print(toke1s.get(char, ''))

print('return 0;}')
