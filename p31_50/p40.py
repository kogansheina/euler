import os
import sys

"""
Champernowne's constant
"""
if __name__ == '__main__':
    
    dtot = [1]
    nextd = 1
    for d in range(1,7):
        nextd *= 10
        dtot.append(nextd)
    dl = [1,1]   # d1 = 1, d10 = 1
    # d30, 31 = 2,0
    v = 20
    d = 30
    while d <= 1000000:
        strd = str(d)
        ff = len(strd)
        for l in range(0,ff):
            d += 1
        v += 1
        if d in dtot:
            strv = str(v)
            print "d=%d v=%d %c" % (d,v,strv[0]) 
            dl.append(int(strv[0])) 
    print dl
    dp = 1
    for d in dl: 
        dp *= d
    print dp       
      
        
