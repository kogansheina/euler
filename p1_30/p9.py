#!/usr/bin/env python
import os
import sys

"""
    the Pitagora triplet which a+b+c = 1000
    
    Pitagora triplet: a**2 + b**2 = c**2
    some math gives: c = (p**2-2*a*b)/(2*p)
    c must be natural, means (p**2-2*a*b)%(2*p) must be 0
"""
if __name__ == '__main__':
    
    from sys import argv
    p = 1000
    if len(argv) == 2:
        p = int(argv[1]) 
    a = 1
    b = 2
    a2 = a**2
    b2 = b**2
    while True:
        c = p-a-b
        c2 = c**2
        if a2+b2==c2:
            print "a=%d b=%d c=%d : a*b*c=%d" % (a,b,c,a*b*c)
            sys.exit()
        elif (b < p-1) and (b > a):
            b += 1
            b2 = b**2
        else:
            a += 1
            a2 = a**2
            if a < p-1:
                b = a+1
                b2 = b**2
            else:
                print "NONE a=%d b=%d c=%d : a*b*c=%d" % (a,b,c,a*b*c)
                sys.exit()
                
          
        
