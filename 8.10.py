l = ['123', '234', '564', '785', '458']
valid = False
count = 3
while count > 0:
	input = raw_input('enter password')
	for i in l:
		if input == i:
			valid = True
			break
	if not valid:
		print 'invalid input'
		count = count - 1
#		continue
	else:
		break