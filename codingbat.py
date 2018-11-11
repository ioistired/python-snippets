#!/usr/bin/env python3
# encoding: utf-8
# Public Domain

def change_x_to_y(word):
	if word:
		first_char = 'y' if word[0] == 'x' else word[0]
		return first_char + change_x_to_y(word[1:])
	else:
		return ''

def change_x_to_y(word, acc=''):
	if word:
		next_char = 'y' if word[0] == 'x' else word[0]
		return change_x_to_y(word[1:], acc + next_char)
	else:
		return acc
