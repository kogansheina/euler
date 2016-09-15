#!/usr/bin/env python
import os

"""
    generate prime number with Eratosthenes sleives
"""
if __name__ == '__main__':
    
    from sys import argv
    primes = []
    A = [False,False]
          
    number = 120000 # generates 11,301 prime numbers
    if len(argv) == 2:
        number = int(argv[1]) 
    for i in range(2,number):
        A.append(True)
    nroot = int(number ** 0.5)
    for i in range(0,nroot+1):
        if A[i]:
            jj = i**2
            for k in range(0,number):
                j = jj+k*i
                if j < number:
                    A[j] = False
                else:
                    break
    for i in range(0,len(A)):
        if A[i]:
            primes.append(i)
    print primes[:20]
    print primes[10000]
    #print primes[10001]
    #print primes[10002]
        
