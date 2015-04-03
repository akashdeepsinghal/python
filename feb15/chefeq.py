#!/usr/bin/python
from collections import Counter

T = int(raw_input())

case=0
while (case<T):
	n=int(raw_input())
	str_array = raw_input()
	int_array = [int(i) for i in str_array.split()]
	mode_counter = Counter(int_array)
	repeat = mode_counter.most_common()[0][1]
	print len(int_array)-repeat
	
	case = case+1