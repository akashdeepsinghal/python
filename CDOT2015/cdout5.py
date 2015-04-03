#!/usr/bin/python
T = int(raw_input())
case=0
while (case<T):
	n, k = map(int, raw_input().split())
	total = 0
	first = k

	if first%2 == 0:
		if n%2==0:
			last = n
		else:
			last = n-1
	else:
		if n%2==0:
			last = n-1
		else:
			last = n
	d = 2
	m = (last-first)/d + 1
	total = m*(first+last)/2
	print total
	case = case+1