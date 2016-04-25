filename = raw_input("please enter the filename:")
n = raw_input(">>>")
try:
	f = open(filename,'r')
#	lines = f.readlines()
#	for j in lines:
#		N = N + 1
#	print N
	for i in range(int(n)):
		print f.readline().strip()
	f.close()
except IOError:
	print "please check the file exist or not."

