#!/usr/bin/python

T = raw_input()
T_list = list(T)
N = len(T)
count = 0
for i in xrange(0,N):
	bet = (i+1)*100
	if T_list[i]=='H':
		count+=bet
	else:
		count-=bet
print count