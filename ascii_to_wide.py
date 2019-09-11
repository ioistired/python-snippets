#!/usr/bin/env python3

table = {i: chr(i + 0xFEE0) for i in range(33, 127)}
table[ord(' ')] = '\N{IDEOGRAPHIC SPACE}'

def ascii_to_fullwidth(text):
	return text.translate(table)

def main():
	assert ascii_to_fullwidth('h') == 'ｈ'

if __name__ == '__main__':
	main()
