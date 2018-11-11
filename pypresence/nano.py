#!/usr/bin/env python3
# encoding: utf-8

# Public Domain
# https://creativecommons.org/publicdomain/zero/1.0/

import getopt
from getpass import getuser
import os.path
import subprocess
import sys
import time

import psutil
import pypresence

def excepthook(_, error, __):
	if not isinstance(error, pypresence.InvalidID):
		sys.__excepthook__(type(error), error, error.__traceback__)

sys.excepthook = excepthook

# how many seconds to spend between updates
DELAY = 3

client = pypresence.Presence('486029858158280716')
while True:
	try:
		client.connect()
	except (ConnectionRefusedError, FileNotFoundError):
		time.sleep(DELAY)
		continue
	else:
		break

def get_nano_processes():
	user = getuser()
	try:
		return tuple(filter(
			lambda process: process.username() == user,
			map(
				lambda line: psutil.Process(int(line.split()[0])),
				subprocess.check_output(['pidof', 'nano']).splitlines())))
	except (psutil.NoSuchProcess, subprocess.CalledProcessError):
		return ()

def process_info(process):
	with process.oneshot():
		running = process.is_running()
		# for some reason my laptop's unix time isn't in UTC??
		start_time = process.create_time()
		cwd = process.cwd()
		command_line = process.cmdline()

	# TODO investigate why nano.open_files() doesn't work here
	return running, start_time, cwd, command_line

def parse_args(command_line):
	try:
		opts, args = getopt.gnu_getopt(
			command_line[1:],
			# short options from nano.c line 2094 at commit fe3a72ce3ea66a568acfdc31ede3b136a20612c9
			'ABC:DEFGHIKLMNOPQ:RST:UVWX:Y:abcdefghijklmno:pqr:s:tuvwxyz$',
			# long options from nano.c line 1964 at commit fe3a72ce3ea66a568acfdc31ede3b136a20612c9
			('boldtext', 'multibuffer', 'ignorercfiles', 'rebindkeypad', 'nonewlines', 'trimblanks', 'morespace', 'quotestr=', 'restricted', 'tabsize=', 'quickblank', 'version', 'syntax=', 'constantshow', 'rebinddelete', 'showcursor', 'help', 'linenumbers', 'mouse', 'noread', 'operatingdir=', 'preserve', 'quiet', 'fill=', 'speller=', 'tempfile', 'view', 'nowrap', 'nohelp', 'suspend', 'smarthome', 'backup', 'backupdir=', 'tabstospaces', 'locking', 'historylog', 'noconvert', 'positionlog', 'smooth', 'wordbounds', 'wordchars=', 'atblanks', 'autoindent', 'cutfromcursor', 'unix', 'afterends', 'softwrap'),
		)
	except getopt.GetoptError:
		# invalid argument
		return True, None, None

	opts = dict(opts)

	if any(x in opts for x in ('-V', '--version', '-h', '--help')):
		return True, None, None

	view_mode = '-v' in opts or '--view' in opts
	filename = args[0] if args else None
	return False, view_mode, filename

def replace_home(filename):
	"""replace $HOME with ~ in the directory and filename"""
	home = os.path.expanduser('~')
	return filename.replace(home, '~')

def on_not_running():
	client.clear()
	time.sleep(DELAY)

def main():
	while True:
		try:
			nano = get_nano_processes()[-1]
		except IndexError:
			on_not_running()
			continue

		running, start_time, cwd, command_line = process_info(nano)
		if not running:
			on_not_running()
			continue

		exited, view_mode, filename = parse_args(command_line)
		if exited:
			on_not_running()
			continue

		if filename is None:
			filename = 'New Buffer'
		else:
			# $HOME replaced with ~ for brevity and anonymity
			filename = replace_home(filename)
		client.update(
			details='Viewing a file' if view_mode else 'Editing a file',
			state=filename.ljust(2),  # make sure it's at least 2 chars
			large_image='nano',
			large_text='fuck your vimrc')
		time.sleep(DELAY)

if __name__ == '__main__':
	try:
		main()
	finally:
		client.clear()
		client.close()
