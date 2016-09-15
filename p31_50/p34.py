import os
import sys

"""
Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""
           
def fact(n):
    if n == 0:
        return 1;
    p = n
    while n > 1:
        n -= 1
        p *= n
    return p
    
if __name__ == '__main__':
    sum = 0
    from sys import argv
    
    number = 1860000 # from Wiki on fractorians
    if len(argv) == 2:
        number = int(argv[1]) 
    for a in range (11,number):
        stra = str(a)
        s = 0
        for c in stra:
            s += fact(int(c))
        if s == a:
            sum += a
            print a
    print sum
            
      
        
