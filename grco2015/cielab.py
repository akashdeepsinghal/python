a, b = map(int, raw_input().split())
if (a-b)%10 == 9:
	print a-b-1
else:
	print a-b+1 