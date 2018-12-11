import sys, os

print('y')

if sys.argv[1] == 'loop':
	os.execve(sys.executable, ['python'] + sys.argv, os.environ)
