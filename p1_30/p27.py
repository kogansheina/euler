import os
import sys
import genprimes

"""
Quadratic primes

Find the product of the coefficients, a and b, for the quadratic expression that produces 
the maximum number of primes for consecutive values of n, starting with n = 0.
"""
if __name__ == '__main__':
    from sys import argv
    
    debug = False
    if len(argv) == 1:
        number = 1000
    else:
        number = int(argv[1])
        if len(argv) > 2:
            debug = True
    prime = genprimes.genPrimes(number)
    longest = (0,0,0)
    # because we start from n=0, we need that b will be a prime number, between 2 and 1000
    for a in range(-number,number):
        #print "a="+str(a)
        for b in range(2,number):
            #print "b="+str(b)
            if b in prime:
                n = 0
                c = 0
                prim = n*n+a*n+b
                while prim in prime:
                    if debug:
                        print "c=%d a=%d b=%d" % (longest[0],longest[1],longest[2])
                        print "n=%d prim=%d" % (n,prim)
                    c += 1
                    if c > longest[0]:
                        longest = (c,a,b)
                    n += 1 
                    prim = n*n+a*n+b
    print "final: count=%d a=%d b=%d" % (longest[0],longest[1],longest[2]) 
    print longest[1]*longest[2]               
                    
        
            
        
        
