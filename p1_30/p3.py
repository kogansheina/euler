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
    
"""
    the greatest prime divider of 600,851,475,143
"""

if __name__ == '__main__':
    
    from sys import argv
    dividers = []
    divpowers = []
             
    number = 600851475143
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genPrimes(number)
    
    for i in range(0,len(prime)):
        residue = number%prime[i]
        if residue == 0:
            dividers.append(prime[i])
            n = number/prime[i]
            p = 1
            while n >= prime[i]:
                if n%prime[i] == 0:
                    p += 1
                    n = n/prime[i]
                else:
                    break
            divpowers.append(p)
            
    print dividers
    print divpowers
