T = int(raw_input())
case=0
while (case<T):
	c=int(raw_input().split()[1])
	desire = raw_input().split()
	k=0
	for i in xrange(0,len(desire)):
		k+=int(desire[i])
	if k<=c:
		print 'Yes'
	else:
		print 'No'
	case = case+1