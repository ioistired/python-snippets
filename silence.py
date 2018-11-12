#!/usr/bin/env python3

import os
import sys
import tempfile

seconds = int(sys.argv[1])
file = sys.argv[2]

with open(tempfile.mktemp(), 'w') as f:
	f.write('; SampleRate 8000\n')
	samples = seconds * 8000
	for i in range(samples):
		f.write(str(i//8000))
		f.write('\t0\n')

os.system(f'sox {f.name} -r 44100 -c 2 {file}')
os.remove(f.name)
