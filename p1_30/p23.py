import os
import sys
import genprimes

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and 
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant 
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
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
    
def search(abundant,limit,notlist):
        
    stop = False
    l = len(abundant)
    for a in range(0,l):
        if stop:
            break
        for b in range(a,l):
            s = abundant[a]+abundant[b]
            if s < limit:
                if s not in notlist:
                    notlist.append(s)
                    #print "a=%d %d, b=%d %d, s=%d" % (a,abundant[a],b,abundant[b],s)
            else:
                #print  "break a=%d b=%d" % (a,b)
                #because the list is sorted then both numbers might be removed
                del abundant[a]
                abundant = abundant[b-1:] # the index is moved because of the previous delete
                stop = True
                break
    return (abundant,notlist)
               
if __name__ == '__main__':
    limit = 28123
    prime = genprimes.genPrimes(limit+1)
    abundant = []
    # - first find all abundant number less than limit
    # - make a list of all numbers which cannot be a sum of 2 of the above numbers
    for n in range(1,limit+1):
        tp = genprimes.foundDividers(n,prime)
        alldiv = allDiv(tp,n) # list of all proper dividers of n
        s = d(alldiv) # sum of all proper dividers
        if n < s: # n is abundant
            abundant.append(n)
    print "first "+str(len(abundant))
    notlist = []
    l = len(abundant)
    while l > 1:
        #if l%100 == 0:
        #    print l
        tp = search(abundant,limit,notlist)
        abundant = tp[0]
        notlist = tp[1]
        l = len(abundant)
    #print notlist
    print "last "+str(len(abundant))
    sum = 0
    for n in range(1,limit):
        if n not in notlist:
            sum += n
            print n
    print sum
    
        
        
        
