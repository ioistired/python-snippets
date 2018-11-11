#!/usr/bin/env python3
# encoding: utf-8

# from lyricly
f=lambda n,i="1":n<2 or(eval(i)<=n if eval(i)>=n else f(n,i+"*%d"%(int(i[-1])+1)))

def f(n, i='1'):
	print(i)
	if n < 2: return True
	if eval(i) >= n:
		return eval(i) == n
	else:
		lastnum = int(i.split('*')[-1])
		return f(n, i+f'*{lastnum+1}')

f=lambda n,i='1':n<2or(eval(i)<=n if eval(i)>=n else f(n,i+'*%d'%(int(i.split('*')[-1])+1)))

def f(n):
	x = 1
	factor = 1
	while x < n:
		factor += 1
		x *= factor
	return x == n
