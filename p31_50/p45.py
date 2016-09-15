import os
import sys
import math

"""
Triangular, pentagonal, and hexagonal

result that H >= P > T for the same i
"""
def gen_triangular(i):
    return i*(i+1)/2
def gen_pentagonal(i):
    return i*(3*i-1)/2  
def gen_hexagonal(i):
    return i*(2*i-1) 
    
if __name__ == '__main__':
    
    k=2
    first = True
    while True: 
        k += 1
        t = gen_triangular(k) 
        j = k-1 
        p = gen_pentagonal(j)
        while p != t and j > 1:
            j -= 1
            p = gen_pentagonal(j)
        if p != t or j == 1:
            continue
        i = j-1
        h = gen_hexagonal(i)  
        while p != h and i > 1:
            i -= 1
            h = gen_hexagonal(i)
        if p == t and i > 1:
            print "found %d %d" % (k,t)
            if first:
                first = False
            else:
                break
