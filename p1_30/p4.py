#!/usr/bin/env python
import os
import sys
"""
palindromic number reads the same both ways
find the largest palindrome made from the product of 3-digit numbers
"""
def check(number):
    s = str(number)
    l = len(s)
    for i in range(0,l/2+1):
        if s[i] != s[l-1-i]:
            return False
    return True
    
if __name__ == '__main__':
    
    for n1 in range(999,100,-1):
        for n2 in range(999,100,-1):
            n = n1*n2
            print "n=%d n1=%d n2=%d" % (n,n1,n2)
            if check(n):
                print n
                sys.exit()
                
