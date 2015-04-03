#!/usr/bin/python
t = int(raw_input())
for i in xrange(0,t):
	count = ''
	string = raw_input()
	string_arr = string.split()
	for j in xrange(0,len(string_arr)):
		count += str(len(string_arr[j]))
	print int(count)