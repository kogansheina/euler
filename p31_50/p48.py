import os
import sys

"""
Self powers
"""
        
if __name__ == '__main__':
    
    number = 1000 
    sum = 10405071317
    for i in range(11,number+1):
        sum += i**i
    ss = str(sum)
    print ss[len(ss)-10:]
