import os
import sys
import genprimes

"""
Distinct primes factors
"""
        
if __name__ == '__main__':
    
    from sys import argv
    
    number = 200000 
    if len(argv) == 2:
        number = int(argv[1]) 
    prime = genprimes.genPrimes(number+1)
    tp2 = (0,0)
    tp3 = (0,0,0)
    tp4 = (0,0,0,0)
    f1 = False
    f2 = False
    print "primes generated"
    for n in range(1,number+1):
        tp = genprimes.foundDividers(n,prime)
        dividers = tp[0]
        divpowers = tp[1]
        if len(dividers) == 2:
            if n == tp2[0]+1:
                if tp2[1] == 0:
                    tp2 = (tp2[0],n)
                    print "2 consecutive : %d %d" % (tp2[0],n)
                    f1 = True
            elif not f1:
                tp2 = (n,0)
        elif len(dividers) == 3:
            if tp3[0] != 0:
                if tp3[1] != 0:
                    if n == tp3[1]+1:
                        if tp3[2] == 0:
                            print "3 consecutive : %d %d %d" % (tp3[0],tp3[1],n)
                            tp3 = (tp3[0],tp3[1],n)
                            f2 = True
                    elif not f2:
                        tp3 = (n,0,0)
                elif n == tp3[0]+1:
                    tp3 = (tp3[0],n,0)
                elif not f2:
                    tp3 = (n,0,0)
            else:
                tp3 = (n,0,0)
        elif len(dividers) == 4:
            print n
            print tp4 
            if tp4[0] != 0:
                if tp4[1] != 0:
                    if tp4[2] != 0:
                        if n == tp4[2]+1:
                            print "4 consecutive : %d %d %d %d" % (tp4[0],tp4[1],tp4[2],n)
                            break
                        else:
                            tp4 = (n,0,0,0)
                    elif n == tp4[1]+1:
                        tp4 = (tp4[0],tp[1],n,0)
                    else:
                        tp4 = (n,0,0,0)
                elif n == tp4[0]+1:
                    tp4 = (tp4[0],n,0,0)
                else:
                    tp4 = (n,0,0,0)
            else:
                tp4 = (n,0,0,0)
