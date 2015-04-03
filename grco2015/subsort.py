#!/usr/bin/python
T = int(raw_input())
case=0
while (case<T):
	n=int(raw_input())
	str_array = raw_input()
	int_array = [int(i) for i in str_array.split()]
	asc_sorted = sorted(int_array)
	if len(int_array)==n:
		for j in xrange(1,n+1):
			if asc_sorted[j-1]!=int_array[j-1]:
				begin = j
				break
		for k in xrange(1,n+1):
			if asc_sorted[n-k-1]!=int_array[n-k-1]:
				end = n-k
				break
		print str(begin)+','+str(end)
		case = case + 1