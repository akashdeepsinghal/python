#!/usr/bin/python

T = int(raw_input())

case=0
while (case<T):
	s=raw_input()
	s_array = list(s)
	s_length = len(s_array)
	change_minus = 0
	for i in xrange(0,s_length):
		if i%2 == 0:
			if s_array[i]=='+':
				change_minus+=1
		else:
			if s_array[i]=='-':
				change_minus+=1

	print min(s_length-change_minus,change_minus)
	case = case+1