#!/usr/bin/python
import math

n, m = map(int, raw_input().split())
str_array = raw_input()
int_array = [int(i) for i in str_array.split()]
total_sum = 0

for i in xrange(0,n):
	fi = 0
	for j in xrange(1,i+2):
		term = (j)*(math.factorial(j)+int_array[i])
		fi+=term
	# print fi
	total_sum+=fi

print total_sum%m