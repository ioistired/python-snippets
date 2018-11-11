#!/usr/bin/env python3
# encoding: utf-8

from lru import LRU
import psutil

process = psutil.Process()

def get_mem_usage():
	return process.memory_full_info().uss

lru = LRU(100)

def fill():
	for i in range(lru.get_size()):
		lru[i] = i+1

fill()

print('Hit LRU max size.')
print(get_mem_usage())

fill()

print('Exceeded LRU max size.')
print(get_mem_usage())

fill()

print('Exceeded LRU max size.')
print(get_mem_usage())

for _ in range(100):
	fill()

print('Exceeded LRU max size.')
print(get_mem_usage())

for _ in range(100):
	fill()

print('Exceeded LRU max size.')
print(get_mem_usage())

for _ in range(100):
	fill()

print('Exceeded LRU max size.')
print(get_mem_usage())
