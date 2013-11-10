#exercise 1

n = raw_input("number")
def divisors(n):
	n = int (n)
	for i in range(n):
		if n%(i+1) == 0:
     			print i+1
divisors(n)

#exercise 2

x=raw_input("Please insert a word")
y=x[::-1]
if x==y:
    print "It's a palindrome"
else:
    print "It's not a palindrome"
    
    
#exersice 3




