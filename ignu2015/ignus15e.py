#!/usr/bin/python

T = int(raw_input())

case=0
while (case<T):
	N=int(raw_input())
	A = map(int, raw_input().split())
	sum_odd=0
	sum_even=0
	for i in xrange(0,N):
		if i%2==1:
			sum_odd+=A[i]
		else:
			sum_even+=A[i]
	print max(sum_even,sum_odd)
	case = case+1