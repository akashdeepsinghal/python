#!/usr/bin/python
n = int(raw_input())
case=0
while (case<n):
	total = 0
	S = raw_input()
	S_chars = list(S)
	S_chars_len = len(S_chars)
	for i in xrange(0,S_chars_len):
		total += ord(S_chars[i])-64
	print total
	case = case+1