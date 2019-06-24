#!/usr/bin/env python3

try:
	1/0
except ZeroDivisionError as e:
	print(e.__original__)  # None or unset?
