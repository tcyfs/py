import time
str = raw_input(">>>>")
n = 0
while n < len(str):
	print str[n],
	n += 1
	time.sleep(1)