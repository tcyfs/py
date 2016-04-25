balance = float(raw_input("Enter opening balance:"))
payment = float(raw_input("Enter monthly payment:"))
print "Amount Remaining"
n = 1 
print "Pymt#   Paid     balance"
print "-----  ------   ---------"
print "0      $ 0.00     $",balance
balance = balance - payment
while balance>=0:
	print n,"     $",payment,"   $",balance
	n = n + 1
	balance = balance - payment
if balance + payment != 0:
	print n,"     $",balance+payment,"    $ 0.00"
print "-----  ------   ---------"