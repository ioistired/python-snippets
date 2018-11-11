#!/usr/bin/env python -tt 
# encoding: utf-8

from __future__ import print_function

import math


def reboot():
	# TODO implement this
	pass


def foo():
	# this will not taberror, even with -tt
	if (  1
	    * 2
	    * 3
	    * 4
	    * 5 != math.factorial(5)):
		print('uh i think my system wack. lemme reboot.')
		reboot()
	else:
		print('ok we good fam 😅')

foo()
