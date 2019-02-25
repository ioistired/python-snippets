#!/usr/bin/env python3
# encoding: utf-8

a = 1

for name, value in globals().items():  # RuntimeError: dictionary changed size during iteration
	print(name, value)
