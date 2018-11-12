#!/usr/bin/env python3
# encoding: utf-8

import sys

TEMPLATE = """
def f%d():
	f%d()
"""

with open('main.py', 'w') as f:
	f.write('#!/usr/bin/env python3\n')
	for i in range(sys.getrecursionlimit()+1):
		f.write(TEMPLATE % (i, i+1))
	f.write('\n')
	f.write('def f%d():\n' % (i+1))
	f.write('\tprint("we made it!")\n')
	f.write('f0()\n')
