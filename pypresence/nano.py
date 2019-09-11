#!/usr/bin/env python3
# encoding: utf-8

# Public Domain
# https://creativecommons.org/publicdomain/zero/1.0/

import getopt
from getpass import getuser
import operator
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
		return sorted(
			filter(
				lambda process: process.username() == user,
				map(
					lambda pid: psutil.Process(int(pid)),
					subprocess.check_output(['pidof', 'nano']).split())),
			key=operator.attrgetter('pid'))
	except (psutil.NoSuchProcess, subprocess.CalledProcessError):
		return []

def process_info(process):
	with process.oneshot():
		running = process.is_running()
		start_time = round(process.create_time() * 1000)
		cwd = process.cwd()
		command_line = process.cmdline()

	# TODO investigate why nano.open_files() doesn't work here
	return running, start_time, cwd, command_line

def parse_args(command_line):
	try:
		opts, args = getopt.gnu_getopt(
			command_line[1:],
			# short options from nano.c line 2039 at commit 7d9ad31cd96cd414d76031d027ee1e194a599858
			'ABC:DEFGHIJ:KLMNOPQ:RST:UVWX:Y:Zabcdeghijklmno:pr:s:tuvwxyz$',
			# long options from nano.c line 1904 at commit 7d9ad31cd96cd414d76031d027ee1e194a599858
			('afterends', 'atblanks', 'autoindent', 'backup', 'backupdir', 'boldtext', 'breaklonglines', 'constantshow', 'cutfromcursor', 'emptyline', 'fill', 'guidestripe', 'help', 'historylog', 'ignorercfiles', 'jumpyscrolling', 'linenumbers', 'locking', 'morespace', 'mouse', 'multibuffer', 'noconvert', 'nohelp', 'nonewlines', 'noread', 'nowrap', 'operatingdir', 'positionlog', 'preserve', 'quickblank', 'quotestr', 'rawsequences', 'rebinddelete', 'restricted', 'showcursor', 'smarthome', 'smooth', 'softwrap', 'speller', 'suspend', 'syntax', 'tabsize', 'tabstospaces', 'tempfile', 'trimblanks', 'unix', 'version', 'view', 'wordbounds', 'wordchars', 'zap'),
		)
	except getopt.GetoptError:
		# invalid argument
		return True, None, None

	opts = dict(opts)

	if any(x in opts for x in ('-V', '--version', '-h', '--help')):
		return True, None, None

	view_mode = '-v' in opts or '--view' in opts
	filename = next((arg for arg in args if not arg.startswith('+')), None)
	return False, view_mode, filename

def replace_home(filename):
	"""replace $HOME with ~ in the directory and filename"""
	home = os.path.expanduser('~')
	return filename.replace(home, '~', 1)

def on_not_running():
	client.clear()
	time.sleep(DELAY)

def main():
	while True:
		try:
			# get the first process instead of the last
			# i usually open up long term files first, so this makes more sense
			nano = get_nano_processes()[0]
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
			large_text="tfw can't be bothered to learn something better",
			start=start_time)
		time.sleep(DELAY)

if __name__ == '__main__':
	try:
		main()
	finally:
		client.clear()
		client.close()
