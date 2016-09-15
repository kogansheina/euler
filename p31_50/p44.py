import os
import sys
import math

"""
Pentagon numbers
pn = n(3n-1)/2

"""
def pe44_old():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        ps.add(p)
        for n in ps:
            if p-n in ps and p-2*n in ps: 
                return p-2*n

def pe44():
    ps = set()
    i = 0
    while True:
        i += 1
        p = (3*i*i - i) / 2
        ps.add(p)
        #p is the greatest number and the last
        for n in ps:
            if p-n in ps and p+n in ps: 
                return p-n
                
if __name__ == '__main__':
    
    print "Project Euler 44 Solution =", pe44_old()        
    print "Project Euler 44 Solution =", pe44()        
      
        
