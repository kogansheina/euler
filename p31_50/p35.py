import os
import sys
import genprimes

"""
Circular primes
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
"""
def checkCircular(a):
    stra = str(a)
    strb = stra[1:len(stra)]
    strb += stra[0]
    return strb
             
if __name__ == '__main__':
    from sys import argv
    
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genprimes.genPrimes(number+1)
    counter = 0
    for i in prime:
        j = checkCircular(i)
        #print "0 -> i=%d j=%s" % (i,j)
        itisnot = True
        while i != int(j):
            if int(j) not in prime:
                itisnot = False
                break
            j = checkCircular(j)
        if itisnot:
            print "i=%d" % i
            counter += 1
    print counter
            
      
        
