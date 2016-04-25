n1 = int(raw_input(">>>"))
n2 = int(raw_input(">>>"))
l1 = []
l2 = []
if n1 > n2:
	for i in range(1, n2 + 1):
		if n1 % i == 0 and n2 % i == 0:
			l1.append(i)
	print l1[-1]
	for j in range(n1, n1 * n2 + 1):
		if j % n1 ==0 and j % n2 == 0:
			l2.append(j)
	print l2[0]
else:
	for i in range(1, n1 + 1):
		if n1 % i == 0 and n2 % i == 0:
			l1.append(i)
	print l1[-1]
	for j in range(n2, n1 * n2 + 1):
		if j % n1 ==0 and j % n2 == 0:
			l2.append(j)
	print l2[0]