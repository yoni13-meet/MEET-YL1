#exercise 1

n = raw_input("number")
def divisors(n):
	n = int (n)
	for i in range(n):
		if n%(i+1) == 0:
     			print i+1
divisors(n)
