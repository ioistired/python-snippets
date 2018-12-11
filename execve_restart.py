#!/usr/bin/env python3
# encoding: utf-8

import sys, os

print('y')

if len(sys.argv) > 1 and sys.argv[1] == 'loop':
	os.execve(sys.executable, ['python'] + sys.argv, os.environ)

# run this script as "./execve_restart.py loop" for the slowest "yes(1)" you will ever see
