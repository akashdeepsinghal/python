#!/usr/bin/python

T = int(raw_input())
ans_array = []
max_count = 0
# print ans_array;
case=0
while (case<T):
	eq_no = 'NO EQUILIBRIUM'
	n=int(raw_input())
	str_array = raw_input()
	int_array = [int(i) for i in str_array.split()]
	if len(int_array)==n:
		for j in xrange(1,n-1):
			lsum = sum(int_array[:j])
			rsum = sum(int_array[j+1:])
			if lsum==rsum:
				eq_no = int_array[j]
				done = 1
				break
		case = case+1
		print eq_no