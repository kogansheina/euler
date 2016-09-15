#!/usr/bin/env python
import os
import sys
"""
the smallest number which is evenly divisible by all numbers from 1 to 20
"""    
if __name__ == '__main__':
    
    n = 1
    primes = [5,7,9,11,13,16,17,19]
    for i in range(0,len(primes)):
        n *= primes[i]
        print "n=%d" % (n)
                
