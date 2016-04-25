#-*- coding:utf-8 -*-
def isprime(n):
	if n<3:
		print n,"is prime."
		return True
	else:
		for i in range(2,n): 
			if n % i == 0:
				print n, "is not prime."
				return False
				break
		else:
			print n,"is prime."
			return True


def getfactors(n):
	l = []
	for i in range(1,n+1):
		if n % i == 0:
			l.append(i)
	print l
num = int(raw_input(">>>>"))
isprime(num)
list = []
while True:
	for i in range(2,num):
		if int(num) % i == 0:
			list.append(i)
			num = num / i
			break
	else:
		list.append(num)
		break
if len(list) == 1:
	list.append(1)
	print list
else:
	print list
