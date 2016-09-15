#!/usr/bin/env python
import os
import sys
    
"""
Longest Collatz sequence
"""
    
if __name__ == '__main__':
    from sys import argv
    
    number = 13
    if len(argv) > 1:
        number = int(argv[1]) 
    if number > 1000000:
        print "Number too big"
        sys.exit()  
    #final = []
    longest = 0
    final = number
    while number < 1000000:  
        collatz = [number]
        n = number
        while n > 1:
            if n%2 == 0:
                n = n/2
            else:
                n = 3*n+1
            collatz.append(n)
        #final.append((number,len(collatz)))
        if longest < len(collatz):
            longest = len(collatz)
            final = number
        number += 1       
    print "Number %d has the longest chain %d" % (final,longest)
