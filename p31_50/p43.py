import os
import sys
import math

"""
Sub-string divisibility
"""
def a2(orig):
    o = orig[:len(orig)-2]
    o.append(orig[-1])
    o.append(orig[-2])
    return [orig,o]
    
def aa(orig,ind):
    subl = orig[len(orig)-ind:]
    suborig = orig[:len(orig)-ind]
    newlist = []
    for i in range(0,ind):
        tmp = list(suborig)
        tmp.append(subl[i])
        if ind == 3:
            ll = a2(subl[0:i]+subl[i+1:])
        else:
            ll = aa(subl[0:i]+subl[i+1:],ind-1)
        for a in ll:
            bb = list(tmp)
            for b in a:
                bb.append(b)
            newlist.append(bb)
    return newlist
    
def check(listelement):
    dividers = [2,3,5,7,11,13,17]
    for i in range(1,8):
        p = listelement[i]*100+listelement[i+1]*10+listelement[i+2]
        if p%dividers[i-1] != 0:
            return False
    return True
    
def makenumber(ll):
    s = ll[-1]
    llen = len(ll)-1
    for e in range(0,len(ll)-1):
        s += ll[e]*(10**(llen))
        llen -= 1
    return s
        
if __name__ == '__main__':
    
    from sys import argv
    
    number = 10 
    if len(argv) == 2:
        number = int(argv[1]) 
    fromlist = []
    for i in range(0,number):
        fromlist.append(i)
    newlist = aa(fromlist,number)
    # newlist contains all the pandigital from 0-9
    print "len newlist="+str(len(newlist))
    counter = 0
    s = 0
    for nl in newlist:
        if check(nl):
            counter += 1
            s += makenumber(nl)
    print "final"
    print counter
    print s
        
      
        
