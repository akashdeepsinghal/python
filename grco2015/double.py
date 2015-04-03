#!/usr/bin/python

T = int(raw_input())
case=0
while (case<T):
	n=int(raw_input())
	if n%2==0:
		print n
	else:
		print n-1
	case = case+1