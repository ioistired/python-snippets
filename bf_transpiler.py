#!/usr/bin/env python3
# encoding: utf-8

import string
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

# allow whitespace to pass through for readability
toke1s.update({c: c for c in string.whitespace})

for line in sys.stdin:
	for char in line:
		print(toke1s.get(char, ''), end='')

print('return 0;}')
