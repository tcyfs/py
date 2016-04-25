import random
N1 = random.randint(1,100)
l = []
L = []
for i in range(N1):
	n = random.randint(0,230)
	l.append(n)
print l
N2 = random.randint(1,100)
for j in range(N2):
	k = l[random.randint(0,N1-1)]
	L.append(k)
print sorted(L)