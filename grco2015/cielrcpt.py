#!/usr/bin/python

def max_two_power(num):
	"This gives a number formed by powers of 2 only and just less than number 'num'"
	i=0
	m=1
	n=1
	while i<=11:
		n=n*2
		if n<=num and i<11:
			i=i+1
		else:
			m=n/2
			break
	return m

T = int(raw_input())
ans_array = []
max_count = 0

case=0
while (case<T):
	p = int(raw_input())

	min_menu = 0
	remaining = p
	while remaining>0:
		max_two = max_two_power(remaining)
		remaining -= max_two
		min_menu += 1
		if remaining==0:
			done = 1
			break

	print min_menu
	case = case+1