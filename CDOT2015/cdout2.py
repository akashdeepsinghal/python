#!/usr/bin/python
T = int(raw_input())
case=0
while (case<T):
	n, k = map(int, raw_input().split())
	n_len = len(str(n))
	number_string = str(n)
	right_sum = 0
	wrong_sum = 0
	for i in xrange(0,n_len):
		dig = int(number_string[i])
		right_mult = dig*10**(n_len-i-1)*k
		if dig==k:
			wrong_mult = dig*10**(n_len-i-1)*2
		else:
			wrong_mult = right_mult
		right_sum += right_mult
		wrong_sum += wrong_mult

	print right_sum+wrong_sum
	case = case+1