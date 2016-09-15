#!/usr/bin/env python
import os
import sys
import genprimes

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ? b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
def d(dividers):
    s = 0
    for a in dividers:
        s += a
    return s
 
def allDiv(tp,number):
    alldiv = [1]
    dividers = tp[0]
    divpowers = tp[1]
    for i in range(0,len(dividers)):
        temp = list(alldiv)
        for j in range(0,len(temp)):
            t = temp[j]*dividers[i]
            if t < number and not t in alldiv:
                alldiv.append(t)
            else:
                break
        for t in range(1,divpowers[i]+1):
            k = dividers[i]**t
            if k < number and not k in alldiv:
                alldiv.append(k)
    return alldiv
           
if __name__ == '__main__':
    from sys import argv
    
    number = 10000
    if len(argv) > 1:
        number = int(argv[1]) 
    amics = []    
    prime = genprimes.genPrimes(10010)
    for n in range(1,number):
        tp = genprimes.foundDividers(n,prime)
        alldiv = allDiv(tp,n)
        # calculate d(n)
        sum = d(alldiv)
        tp = genprimes.foundDividers(sum,prime)
        alldiv = allDiv(tp,sum)
        # calculate d(sum)
        sumpair = d(alldiv)
        if n == sumpair and n != sum:
            if (sum,n) not in amics:
                amics.append((n,sum)) 
        #if n == sumpair:
        #    if n == sum:
        #        amics.append((n,sum)) 
        #    elif (sum,n) not in amics:
        #        amics.append((n,sum)) 
                
    print amics
    sum = 0
    for t in amics:
        sum += t[0]+t[1]
    #for t in amics:
    #    sum += t[0]
    #    if t[0] != t[1]:
    #        sum += t[1]
    print sum
    
         
        
