#!/usr/bin/env python
import os
import sys
"""
n2 = is the square of the sum of all numbers from 1 to 100
n = is the sum of the suares of all numbers from 1 to 100
"""    
if __name__ == '__main__':
    
    n = 1
    for i in range(2,101):
        n += i
    n2 = n*n
    print "n2=%d" % (n2)
    n = 1
    for i in range(2,101):
        n += i*i
    print "n=%d" % (n)
    print n2-n    
                
