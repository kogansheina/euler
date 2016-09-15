#!/usr/bin/env python
from itertools import *
""""
Powerful digit sum
"""
def main():
    maxsum = 0
    for a in range(2,100):
        for b in range(2,100):
            n = a**b
            strn = str(n)
            sum = 0
            for s in strn:
                sum += ord(s)-ord('0')
            if sum > maxsum:
                maxsum = sum
    print "maxsum=%d a=%d b=%d" % (maxsum,a,b)
if __name__ == "__main__":
    main()


