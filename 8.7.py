l=[]
def getfactors(n):
	for i in range(1,n):
		if n % i == 0:
			l.append(i)
num = int(raw_input(">>>>"))
getfactors(num)
if sum(l) == int(num):
	print num,'is perfect!'
else:
	print num,'is not perfect!'
