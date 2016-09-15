import os
import sys
import math
"""
Combinatoric selections
"""
                      
if __name__ == '__main__':
    
    cc = 0
    for n in range(23,101):
        N=math.factorial(n)
        for r in range(1,n):
            R=math.factorial(r)
            M=math.factorial(n-r)
            C = N/R/M
            if C > 1000000:
                cc += 1
    print cc
