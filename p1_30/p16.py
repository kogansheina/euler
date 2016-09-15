#!/usr/bin/env python
import os
"""
    sum of digits of 2**1000
"""
def main(limit):
    n = 2**limit
    d = n/10
    q = n%10
    sum = 0
    #print ("d=%d q=%d") % (d,q)
    while d >= 10:
        sum += q
        q = d%10
        d = d/10
        #print ("d=%d q=%d") % (d,q)
    sum += d+q    
    print "sum = %d" % (sum) 
    
if __name__ == '__main__':
    
    from sys import argv
    
    if len(argv) == 1:
        main(1000)
    else :
        main(int(argv[1]))
