import os
import sys

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
Find the sum of all products whose multiplicand/multiplier/product identity can be written as 
a 1 through 9 pandigital.
"""
def check(strn):
    if "0" in strn:
        return False
    for i in range(1,10):
        stri = str(i)
        if stri not in strn:
            return False
    return True    
           
if __name__ == '__main__':
    br = []
    for a in range (2,100000000):
        sa = "1"
        lena = len(str(a))
        for i in range(0,9-lena):
            sa += "0"
        numbers = int(sa)
        for b in range(1,numbers):
            lenb = len(str(b))
            k = a*b 
            total = lena+lenb+len(str(k)) 
            if total > 9:
                break 
            elif total == 9:
                r = check(str(a)+str(b)+str(k))
                if r:
                    #print "a=%d b=%d k=%d ==> %s" % (a,b,k,r)
                    if k not in br:
                        br.append(k)
    s = 0
    print br
    for b in br:
        s += b
    print s                                  
        
            
        
        
