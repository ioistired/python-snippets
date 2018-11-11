#!/usr/bin/env python3
# encoding: utf-8

""" determine whether s has balanced parentheses """
def is_correct(s):
	counter = 0
	
	for char in s:
		if char == '(':
			counter += 1
		if char == ')':
			counter -= 1
		
		# close paren encountered before open paren
		if counter < 0:
			return False
	
	return counter == 0


def test_is_correct():
	assert is_correct('()')
	assert not is_correct(')(')
	assert not is_correct('foo) ()')
	assert is_correct('(* foo *)()')
	assert not is_correct('())(()')
