import os
import sys


"""
Reciprocal cycles

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.
"""
def temp(d,m):

    q = -1
    m *= 10 
    while m < d:
        q -= 1
        m *= 10
    return (m,q)
    
if __name__ == '__main__':
    from sys import argv
    
    debug = False
    if len(argv) == 1:
        N = 1000
    else:
        N = int(argv[1])
        if len(argv) > 2:
            debug = True
    prev = 1   
    maxperiod = (0,0) 
    lowlim = 2
    highlim = N
    if debug:
        lowlim = N
        highlim = N+1
    for d in range(lowlim,highlim):
        rettp = temp(d,1)
        divided = rettp[0]
        q = rettp[1]
        divlist = []
        prev = [divided]
        fix = True
        while True:
            rest = divided % d
            if rest == 0:
                break
            divstr = str(divided / d)
            while q < 0:
                try:
                    divlist.append(divstr[q])
                except IndexError:
                    divlist.append(0)
                q += 1
            rettmp = temp(d,rest)
            divided = rettmp[0]
            q = rettmp[1]
            if divided in prev:
                fix = False
                break
            else:
                prev.append(divided)
        if fix:
            continue
        periodlen = len(divlist)-prev.index(divided)
        if maxperiod[1] < periodlen:
            maxperiod = (d,periodlen)
        if debug:
            print "checklist : %d %d" % (d,periodlen)
            print maxperiod
    print "d=%d maxperiod=%d" % (maxperiod[0],maxperiod[1])                
                    
        
            
        
        
