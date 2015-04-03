#!/usr/bin/python
# Algo:- http://pitcher.digitalfreehold.ca/code/computeSize
import math

T = int(raw_input())
case=0
while (case<T):
	n=int(raw_input())
	str_array = raw_input()
	int_array = [int(i) for i in str_array.split()]
	if len(int_array)==n:
		clubs = '';
		for j in xrange(0,n):
			k=0
			sum_log=0
			if int_array[j]==1:
				club_no = '1'
			else:
				while (k<int_array[j]):
					sum_log = sum_log+math.log(int_array[j]-k,10)
					k = k+1
				club_no = str(int(math.ceil(sum_log)))
			clubs = clubs+club_no+' '

		# fact = fact+str(len(str(math.factorial(int_array[j]))))+' ';
		print clubs
		case = case+1