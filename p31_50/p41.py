import os
import sys

"""
Pandigital prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once
What is the largest n-digit pandigital prime that exists?
"""
def is_prime(n):
    if n == 1:
        return False
    elif n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def check_pandigital(strn):
    if "0" in strn:
        return False
    n = len(strn)
    listn = list(strn)
    for i in range(1,n+1):
        stri = str(i)
        if stri not in listn:
            return False
        listn.remove(stri)
    return True    
           
if __name__ == '__main__':
    
    MAX = 987654321
    maxn = 1
    for n in range(1,MAX+1): #1000000000
        if is_prime(n):
            #print n
            if check_pandigital(str(n)):
                print "TRUE n=%d"  % n
                if maxn < n:
                    maxn = n
    print maxn
        
      
        
