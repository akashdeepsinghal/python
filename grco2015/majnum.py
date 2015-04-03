#!/usr/bin/python

T = int(raw_input())
ans_array = []
max_count = 0
# print ans_array;
case=0
while (case<T):
	major = 'NO'
	n=int(raw_input())
	str_array = raw_input()
	int_array = [int(i) for i in str_array.split()]
	if len(int_array)==n:
		# print 'yo'
		# int_array.sort()
		done = 0
		for j in xrange(0,n):
			count = int_array.count(int_array[j])
			if count>(n/2):
				# ans_array.append(max_count_num)
				major = int_array[j]
				done = 1
				break
		case = case+1
		print major