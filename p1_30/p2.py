#!/usr/bin/env python
import os

"""
    sum of even Fibonacci nymbers below 4,000,000
"""
def main(limit):
    fib = [1,2]
    
    doloop = True
    while doloop:
        listlen = len(fib)
        newfib = fib[listlen-2] + fib[listlen-1]
        if newfib >= limit:
            doloop = False
        else:
            fib.append(newfib)
            
    print fib
    sum = 0
    for i in range(0,len(fib)):
        if fib[i]%2 == 0:
            sum += fib[i]
    print "sum = %d" % (sum) 
       
if __name__ == '__main__':
    from sys import argv
    
    if len(argv) == 1:
        main(4000000)
    else :
        main(int(argv[1]))
