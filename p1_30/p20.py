#!/usr/bin/env python
import os
import sys
# sum of the digits of the factorial of Number - 100(default)

def fact(n):
    p = n
    while n > 1:
        n -= 1
        p *= n
    return p
    
if __name__ == '__main__':
    from sys import argv
    
    number = 100
    if len(argv) > 1:
        number = int(argv[1]) 
    N = fact(number)
    print N
    sum = 0
    while N >= 10:
        r = N % 10
        sum += r
        N = N/10
    sum += N
    print sum
         
        
