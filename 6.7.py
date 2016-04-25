num_str = raw_input("Enter a number:")
num_num = int(num_str)
fac_list = range(1, num_num + 1)
print 'BEFORE:', fac_list
n = 0
while n < len(fac_list):
	if num_num % fac_list[n] == 0:
		del fac_list[n]
	else:
		n = n + 1

print 'AFTER:', fac_list