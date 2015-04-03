#!/usr/bin/python
import math
T = int(raw_input())

case=0
while (case<T):
	n, k = map(int, raw_input().split())
	n = n+1-k
	num = 1
	den = 1
	k_max = max(n-k,k)
	k_min = n-k_max
	# print n
	# print k_max
	# print k_min
	for i in xrange(k_max+1,n+1):
		num*=i
	for j in xrange(1,k_min+1):
		den*=j
	# print num
	# print den
	# print (math.factorial(n)/((math.factorial(k))*(math.factorial(n-k))))%100003
	print (num/den)%100003
	case = case+1