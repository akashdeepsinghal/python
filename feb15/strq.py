#!/usr/bin/python

string = list(raw_input())
Q = int(raw_input())

for k in xrange(0,Q): #No. of cases
	total_sum = 0
	a,b,L,R = raw_input().split()
	# L,R = map(int,[L,R])
	L = int(L)
	R = int(R)

	for i in xrange(L-1,R):
		if string[i]==a:
			total_sum += string[i+1:R].count(b)
	print total_sum