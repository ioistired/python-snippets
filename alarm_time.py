#!/usr/bin/env python3
# encoding: utf-8

def alarm_time(day, is_vacation: bool) -> int:
	"""search for "alarmTime day isVacation" on Homework Help discord for context"""
	
	is_weekend = day in (0, 6)
	
	if is_vacation:
		if is_weekend: return 12
		else: return 10 # weekday
	else:
		if is_weekend: return 10
		else: return 7 # weekday
