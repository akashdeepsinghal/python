#!/usr/bin/python
t = int(raw_input())
case=0
while (case<t):

	in_str = raw_input()
	in_str_list = list(in_str)
	in_str_list_len = len(in_str_list)
	final_list = ['']*in_str_list_len
	for i in xrange(0,in_str_list_len):
		ascii_val = ord(in_str_list[i])
		if ascii_val>=48 and ascii_val<=57:
			final_list[i]=str((int(in_str_list[i])+5)%10)
		elif 97<=ascii_val<=109 or 65<=ascii_val<=77:
			ascii_val += 13
			final_list[i] = chr(ascii_val)
		elif 110<=ascii_val<=122 or 78<=ascii_val<=90:
			ascii_val -= 13
			final_list[i] = chr(ascii_val)
		elif ascii_val == 32:
			final_list[i] = ' '
	final = ''.join(final_list)
	print final
	case = case+1