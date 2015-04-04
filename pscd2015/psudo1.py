#!/usr/bin/python
t = int(raw_input())
case=0
while (case<t):
	total = 0
	times = raw_input().split()
	times_len = len(times)
	for i in xrange(0,times_len):
		hh, mm = map(str,times[i].split(':'))
		if hh==mm or hh==mm[::-1] or (list(hh)[0]==list(hh)[1] and list(mm)[0]==list(mm)[1]):
			total += 1
	print total
	case = case+1