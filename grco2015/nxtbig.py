#!/usr/bin/python

T = int(raw_input())
done = 0
case=0
while (case<T):
	n=int(raw_input())
	str_array = raw_input()
	str_array_split = str_array.split()
	int_array = [int(i) for i in str_array.split()]

	# Printing simple number as it is:-
	k=0
	p = ''
	while k<len(str_array_split):
		p = p + str_array_split[k]
		k = k + 1
	p = int(p)

	if len(int_array)==n:
		m=n
		temp = 0
		while m>1:
			if ((int_array[m-1]>int_array[m-2]) and 1==1):
				ls = int_array[:m-2]
				ls.append(int_array[n-1])
				rs = sorted(int_array[m-2:n-1])
				final_int_array = ls+rs
				int_array = final_int_array
				done = 1
				break
			else:
				m=m-1
		if done==1:
			nxt_big = ''
			#printing the 'Next Big Number':-
			j=0
			while j<len(int_array):
				nxt_big = nxt_big + str(int_array[j])
				j = j + 1
			nxt_big = int(nxt_big)
		else:
			nxt_big = 'NO NXTBIG'
		print p
		print nxt_big
		print type(p)
		print type(nxt_big)

		case = case+1