import os
import sys
from itertools import *
"""
Permuted multiples
"""
def family(n):
    for t in permutations(str(n)):
        yield int(''.join(t))
                      
if __name__ == '__main__':
    
    n = 10000
    doit = True
    while doit:
        cc2=False
        cc3=False
        cc4=False
        cc5=False
        cc6=False
        for i in family(n):
            if n*2 == i:
                cc2 = True
            elif n*3 == i:
                cc3 = True
            elif n*4 == i:
                cc4 = True
            elif n*5 == i:
                cc5 = True
            elif n*6 == i:
                cc6 = True
            if cc2 and cc3 and cc4 and cc5 and cc6:
                print "n=%d i=%d : %d %d %d %d %d" % (n,i,n*2,n*3,n*4,n*5,n*6)
                doit = False
                break
        n += 1
        if n%50000 == 0:
            print n
