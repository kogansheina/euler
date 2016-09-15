#!/usr/bin/env python
import os

"""
    generate prime number with Eratosthenes seives
"""
def genPrimes(number):
    primes = []
    A = [False,False]
          
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
    return primes
    
if __name__ == '__main__':
    
    from sys import argv
    number = 2000000
    if len(argv) == 2:
        number = int(argv[1]) 
    primes = genPrimes(number)
    sum = 0
    for i in range(0,len(primes)):
        sum += primes[i]
    print sum
        
