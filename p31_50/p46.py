import os
import sys
import genprimes
import math

"""
Goldbach's other conjecture
"""
def check(n,primes):
    ok = False
    for a in primes:
        c = n-a
        if c%2 == 0 and c >= 0:
            b = c/2
            try:
                sqb = math.sqrt(b)
                if int(sqb) == sqb:
                    ok = True
                    break
            except ValueError:
                print "error "
                print b
    #if ok:
    #    print "need prime larger"
    return ok
        
if __name__ == '__main__':
    
    from sys import argv
    
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genprimes.genPrimes(number+1)
    n = 35
    while True:
        if check(n,prime):
            n += 2
        else:
            break
    print n
    print prime[-1]
