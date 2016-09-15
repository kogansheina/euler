import os
import sys
import genprimes

prime = []
"""
Consecutive prime sum
"""
def lookit(start,p):
    s = 0
    crtlist = []
    for i in prime[start:]:
        s += i
        if s > p:
            return (2,None)
        else:
            crtlist.append(i)
            if s == p:
                return (1,crtlist)
    return (0,None) 
                  
if __name__ == '__main__':
    
    from sys import argv
    
    listlong = []
    lenlist = 0
    psaved = 0
    number = 1000000 
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genprimes.genPrimes(1000001)
    startindex = prime.index(41)
    for p in prime[startindex:]:
        if p > number:
            break
        start = 0
        while prime[start] <= p: 
            tp = lookit(start,p)
            if tp[0] == 1:
                if len(tp[1]) > lenlist:
                    psaved = p
                    listlong = list(tp[1])
                    lenlist = len(listlong)
                    print "p=%d %d" % (psaved,lenlist)
            elif tp[0] == 0:
                break
            start += 1
    print listlong
    print lenlist
    print psaved
            
    
                                 
    
