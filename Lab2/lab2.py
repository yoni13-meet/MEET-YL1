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

import random
def flip():
    n = raw_input("insert n for next")
    if n == "n":
        a = random.randint(1,2)          
        if a == 1:
            print "T"
        else:
            print "H"


def chance():
    to_flip_heads = raw_input("what is the probability for heads")
    a = random.randint(1, 100)
    if a < to_flip_heads:
        print "heads"
    else:
        print "tails"

def decide_flips():
    t_counter=0
    h_counter=0
    n = int (raw_input("how many times to flip the coin?"))
    for i in xrange(n):
        a = random.randint(1,2)          
        if a == 1:
            print "T"
            t_counter +=1
        else:
            print "H"
            h_counter +=1
            
    print str(t_counter) + "times tails"
    print str(h_counter) + "times heads"

#exercise 4











