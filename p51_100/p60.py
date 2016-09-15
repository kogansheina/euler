#!/usr/bin/env python
import os
import sys
import genprimes

""""
Prime pair sets
13 + 5197 + 5701 + 6733 + 8389 = 26033
"""

def is_prime(n):
    if n == 1:
        return False
    elif n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def main(number):
    prime = genprimes.genPrimes(number)
    print "*****************  "+str(len(prime))
    lowest = -1
    mylist = {}
    for i1 in range(0,len(prime)):
        p1 = prime[i1]
        for i2 in range(i1+1,len(prime)):
            p2 = prime[i2]
            strv = str(p1)+str(p2)   
            if is_prime(int(strv)):
                strv = str(p2)+str(p1)   
                if is_prime(int(strv)):
                    try:
                        mylist[p1].add(p2)
                    except KeyError:
                        mylist[p1] = set([p2])
    aList = set(mylist.keys())
    #for a in aList:                  
    #    print a,mylist[a]
    print "$$$$$$$$$$$$  "+str(len(aList))
    for a in aList:
        if a > lowest and lowest > 0:
            break
        sorteda = sorted(mylist[a])   # a sorted list of unique elements 
        for b in sorteda:
            if lowest > 0 and lowest < a+b:
                break
            try: 
                forC = mylist[a] & mylist[b]
                if len(forC)==0:
                    continue
                sortedforC = sorted(forC)
                for c in sortedforC:
                    if lowest < a+b+c and lowest > 0:
                        break
                    forD = forC & mylist[c]
                    if len(forD)==0:
                        continue
                    sortedforD = sorted(forD)
                    for d in sortedforD:
                        if lowest < a+b+c+d and lowest > 0:
                            break
                        forE = forD & mylist[d]
                        if len(forE)==0:
                            continue
                        sortedforE = sorted(forE)
                        for e in sortedforE:
                            if lowest < a+b+c+d+e and lowest > 0:
                                break
                            lowest = a+b+c+d+e
                            print a,b,c,d,e,lowest
            except KeyError:
                continue
                 
    print lowest                   
if __name__ == "__main__":
    from sys import argv
    number = 10000 
    if len(argv) == 2:
        number = int(argv[1]) 
    main(number)


