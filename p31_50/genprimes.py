Enter file contents here#!/usr/bin/env python
import os
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
    
def foundDividers(number,prime):
        
    dividers = []
    divpowers = []
    
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
            
    return (dividers,divpowers)
