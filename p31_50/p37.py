import os
import sys
import genprimes

"""
Truncatable primes
"""
def truncateLeft(s):
    if len(s) <= 1:
        return None
    return s[1:]
                        
def truncateRight(s):
    if len(s) <= 1:
        return None
    return s[:len(s)-1]

if __name__ == '__main__':
    from sys import argv
    
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    primes = genprimes.genPrimes(number+1)
    counter = 0
    sum = 0
    for i in primes:
        if i == 2 or i == 3 or i == 5 or i == 7:
            continue
        trleft = truncateLeft(str(i))
        isit = True
        while trleft != None:
            if int(trleft) not in primes:
                isit = False
                break;
            trleft = truncateLeft(trleft)
        if isit:
            #print "i=%d " % (i)
            trright = truncateRight(str(i))
            while trright != None:
                if int(trright) not in primes:
                    isit = False
                    break;
                trright = truncateRight(trright)
            if isit:
                print "ok i=%d " % (i)
                counter += 1
                if counter <= 11:
                    sum += i
                else:
                    break
    print counter
    print sum
            
      
        
